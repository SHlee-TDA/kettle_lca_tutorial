"""Normalize the supplied finished BOM to one good output, not a complete LCI."""

import csv
import hashlib
import json
import math
import platform
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOM = ROOT / "data/foreground/kettle-bom.csv"
CONFIG = ROOT / "data/foreground/production-scenarios.json"
OUT = ROOT / "results/inventory"


def normalize(rows, defect_rate):
    if not math.isfinite(defect_rate) or not 0 <= defect_rate < 1:
        raise ValueError("Defect rate must be finite and in [0, 1).")
    attempts = 1 / (1 - defect_rate)
    items = []
    for row in rows:
        mass = float(row["finished_mass_g"]) / 1000
        if not math.isfinite(mass) or mass <= 0:
            raise ValueError("BOM mass must be finite and positive.")
        scope = row["scope"]
        if scope not in {"Kettle", "Packaging"}:
            raise ValueError(f"Unknown BOM scope: {scope}")
        multiplier = attempts if scope == "Kettle" else 1
        items.append({
            "material": row["material"], "scope": scope,
            "retained_in_good_output_kg": mass,
            "finished_component_or_packaging_demand_kg": mass * multiplier,
            "material_in_rejected_assemblies_kg": mass * (multiplier - 1),
            "gross_raw_material_purchase_kg": None,
            "fabrication_scrap_kg": None,
        })
    kettle = sum(i["finished_component_or_packaging_demand_kg"] for i in items if i["scope"] == "Kettle")
    packaging = sum(i["finished_component_or_packaging_demand_kg"] for i in items if i["scope"] == "Packaging")
    retained = sum(i["retained_in_good_output_kg"] for i in items)
    rejects = sum(i["material_in_rejected_assemblies_kg"] for i in items)
    balance = math.isclose(kettle + packaging, retained + rejects, abs_tol=1e-12)
    if not balance:
        raise ValueError("Finished-material balance failed.")
    return {
        "defect_rate": defect_rate,
        "assembly_attempts_per_good_unit": attempts,
        "rejected_assemblies_per_good_unit": attempts - 1,
        "finished_kettle_component_demand_kg": kettle,
        "finished_packaging_demand_kg": packaging,
        "rejected_kettle_material_kg": rejects,
        "finished_material_balance_passed": balance,
        "items": items,
    }


def check_model():
    """Check an independently soluble batch: four starts, three good outputs."""
    rows = [
        {"material": "Example body", "finished_mass_g": "300", "scope": "Kettle"},
        {"material": "Example box", "finished_mass_g": "30", "scope": "Packaging"},
    ]
    case = normalize(rows, 0.25)
    assert math.isclose(case["finished_kettle_component_demand_kg"], 0.4)
    assert math.isclose(case["rejected_kettle_material_kg"], 0.1)
    assert math.isclose(case["finished_packaging_demand_kg"], 0.03)
    assert normalize(rows, 0)["rejected_kettle_material_kg"] == 0
    for invalid in [-0.1, 1, float("nan")]:
        try:
            normalize(rows, invalid)
        except ValueError:
            continue
        raise AssertionError("Invalid defect rate was accepted.")


def main():
    check_model()
    config = json.loads(CONFIG.read_text())
    # ponytail: one inspection gate; implement stage/rework balances before extending.
    required = {"good_output_units": 1, "inspection_stage": "after_complete_assembly_before_packaging",
                "rework": False, "component_salvage": False,
                "reject_composition": "same_finished_material_composition_as_one_kettle",
                "packaging_rejects_modelled": False}
    if any(config.get(key) != value for key, value in required.items()):
        raise ValueError("Unsupported production assumptions; update the model before use.")
    unresolved = ["baseline_defect_rate", "component_fabrication_yields", "packaging_conversion_yields",
                  "assembly_energy_kwh_per_attempt", "inspection_energy_kwh_per_attempt",
                  "packaging_energy_kwh_per_good_unit", "reject_treatment"]
    if any(config.get(key) is not None for key in unresolved):
        raise ValueError("This partial model does not yet implement yields, energy or treatment inputs.")
    if not config["scenario_defect_rates"]:
        raise ValueError("At least one illustrative scenario is required.")
    with BOM.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 12 or len({r["material"] for r in rows}) != 12:
        raise ValueError("Expected the 12 distinct source BOM entries.")
    totals = {s: sum(float(r["finished_mass_g"]) for r in rows if r["scope"] == s)
              for s in ["Kettle", "Packaging"]}
    if not math.isclose(totals["Kettle"], 723) or not math.isclose(totals["Packaging"], 137.8):
        raise ValueError("BOM totals do not match the agreed BC1 specification.")
    cases = [normalize(rows, d) for d in config["scenario_defect_rates"]]
    result = {
        "status": "partial_foreground_inventory_illustration",
        "functional_unit": config["functional_unit"],
        "python_version": platform.python_version(),
        "input_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in [BOM, CONFIG]},
        "assumptions": config, "bom_totals_g": totals,
        "baseline_lci": None, "gwp100_kg_co2eq": None,
        "scenarios": cases,
    }
    lines = ["# Foreground Inventory: Illustrative Defect Scenarios", "",
             "Generated by `python3 src/inventory.py` from the preserved BOM and production-scenarios.json.", "",
             "**Partial foreground calculation only. No baseline defect rate, purchased raw-material quantities, cumulative LCI or GWP100 has been established.**", "",
             config["functional_unit"], "",
             "Inspection follows complete assembly and precedes packaging. No rework or component salvage is modelled. Packaging is applied only to accepted units. Reject treatment is unresolved. Rates are illustrative assumptions, not observed factory data.", "",
             "| Defect rate | Assembly attempts / good unit | Finished kettle components (g / good unit) | Finished packaging (g / good unit) | Rejected kettle material (g / good unit) |",
             "|---:|---:|---:|---:|---:|"]
    for c in cases:
        lines.append(f"| {c['defect_rate']:.0%} | {c['assembly_attempts_per_good_unit']:.6f} | {c['finished_kettle_component_demand_kg'] * 1000:.4f} | {c['finished_packaging_demand_kg'] * 1000:.4f} | {c['rejected_kettle_material_kg'] * 1000:.4f} |")
    lines += ["", "## Material-level finished demand", "",
              "Amounts below are finished components or converted packaging delivered to the modelled assembly/packaging steps, not gross purchases of resin, metal or paper feedstock.", "",
              "| Material | Scope | " + " | ".join(f"{c['defect_rate']:.0%} defects (g/good unit)" for c in cases) + " |",
              "|---|---|" + "---:|" * len(cases)]
    for index, row in enumerate(rows):
        quantities = " | ".join(f"{c['items'][index]['finished_component_or_packaging_demand_kg'] * 1000:.4f}" for c in cases)
        lines.append(f"| {row['material']} | {row['scope']} | {quantities} |")
    lines += ["", "## Checks and interpretation", "",
              "Passed: source BOM totals, model boundary cases and the finished-material balance (component plus packaging demand equals good-output mass plus rejected-assembly mass). This is not a full factory mass balance.", "",
              "Higher final-assembly rejection increases upstream component demand and assembly/inspection activity per good product. It leaves finished packaging demand unchanged under this inspection placement. It does not establish an equal percentage increase in total GWP100: packaging, reject treatment, process yields and characterization remain to be resolved.", "",
              "Fabrication scrap, packaging conversion losses, electricity, transport, supplier closure and environmental flows are not calculated. The detailed JSON preserves these distinctions. No recycling credit is inferred from the absence of component salvage.", ""]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "defect-scenarios.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    (OUT / "defect-scenarios.md").write_text("\n".join(lines))
    print("PASS: source BOM, scenario normalization and model checks")
    print("Wrote results/inventory/defect-scenarios.json and defect-scenarios.md")


if __name__ == "__main__":
    main()
