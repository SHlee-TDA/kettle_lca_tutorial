# Inventory Development: One Conforming Packaged Kettle

Date: 2026-10-08. Status: **initial foreground model with illustrative reject-rate scenarios**. A complete upstream life cycle inventory and LCIA have not been calculated. The [source review](source-review.md) verifies the supplied aggregate BOM against the original report.

## 1. Production output and acceptance

Study-specific production functional unit:

> Provision of one conforming, fully assembled and packaged BC1 1 L electric kettle at the factory gate.

The modelled good output matches the BC1 specification and passes assembly and functional inspection. Actual inspection protocols and thresholds are unknown; no certification is claimed. The exercise's declared unit remains one packaged kettle. Both descriptions refer to the same physical output, while the functional-unit wording makes conformity explicit.

The defect rate changes the inputs required per good output. A measured or assumed defect rate is not a prerequisite for defining the output unit. The 1 L rating is capacity, not a quantity of water heated during the study.

## 2. Separate three inventories

1. **Retained finished mass:** material physically present in one accepted kettle and its packaging; provided by the BOM.
2. **Foreground requirements:** finished components, purchased raw materials, conversion services, energy and transport required to obtain that good output, including justified losses.
3. **Cumulative elementary-flow inventory:** emissions and resource extraction after linking and solving upstream processes. This is not yet available.

The present calculation establishes part of item 2. It does not treat BOM mass as either gross raw-material purchase or environmental emissions.

## 3. Agreed reject-rate illustration

The user selected a simple model with inspection **after assembly and before packaging**, without rework. Defect rates of 0%, 2% and 5% are illustrative sensitivity cases, not measurements or a selected baseline rate.

For the initial calculation, Codex additionally models each rejected assembly as containing the complete kettle BOM, with no component salvage, and packaging only accepted units. These are explicit simplifications. Recycling or disposal of rejects, possible credits and packaging conversion losses remain unresolved. No component recovery or avoided-production credit is calculated.

Let:

- `d` = rejected fraction of complete assembly attempts, dimensionless, with `0 <= d < 1`.
- `m_i` = finished mass of component material i retained in one good kettle, kg.
- `p_j` = finished packaging mass of material j for one accepted kettle, kg.
- `y_i` = component fabrication yield, separate from final-assembly rejection.

For one good output:

```text
Assembly attempts                         N = 1 / (1 - d)
Rejected assembly equivalents             R = d / (1 - d)
Finished kettle component requirement      q_i = m_i / (1 - d)
Material contained in rejected assemblies  w_i = m_i * d / (1 - d)
Finished packaging requirement             q_pack,j = p_j
```

Fractional assembly counts are average requirements over production, not a claim that a fraction of a physical kettle is assembled.

If a simple single-pass fabrication yield is later established, without internal recycling:

```text
Gross raw-material input       a_i = m_i / [(1 - d) * y_i]
Fabrication scrap              s_i = a_i - q_i
Material balance               a_i = m_i + w_i + s_i
```

Packaging conversion requires its own yield. Do not divide packaging by `(1 - d)` when the rejected kettle is identified before packaging. If inspection occurs after packaging, or parts are salvaged/reworked, revise the process model before using these equations.

Assembly and inspection energy per attempt scale by `N`; packaging energy per accepted output scales by one under this model. All energy intensities remain unknown, including any water/electricity used for factory testing. Such testing is a production activity, even though consumer use is excluded.

## 4. Reproducible numerical illustration

[Scenario assumptions](../data/foreground/production-scenarios.json) and the unchanged [BOM](../data/foreground/kettle-bom.csv) are inputs to [the calculator](../src/inventory.py). Run from the project root:

```sh
python3 src/inventory.py
```

Read the generated [English report](../results/inventory/defect-scenarios.md) or [detailed JSON](../results/inventory/defect-scenarios.json). The script uses only the Python standard library and records its Python version and input hashes. It validates the BOM, invalid defect rates, the fixed inspection configuration and a known batch example.

At 2% defects, finished component demand is 737.7551 g per good kettle, of which 14.7551 g is in rejected assemblies; finished packaging remains 137.8000 g. Purchased raw materials, fabrication scrap, treatment inventories and GWP100 remain uncalculated. Scenario outputs are kept outside the reserved independent LCA run.

## 5. Background-data worklist

The following are **candidate process requirements and search terms, not selected dataset matches**. Geography/year, exact grades, IDs, system boundaries, yields and suppliers are unresolved for every row.

| BOM entry | Initial search terms / required functions | Important unresolved distinction |
|---|---|---|
| Stainless steel | stainless steel production; sheet; forming | Alloy, product form and primary/secondary route |
| Brass | brass; copper-zinc alloy; forming | Alloy composition and conversion route |
| Copper | copper production; wire drawing | Physical form and whether wire processing is appropriate |
| PP | polypropylene resin; injection moulding | Grade and resin-only versus converted-product boundary |
| PVC | PVC compound; extrusion | Flexible/rigid grade, additives and actual part function |
| Nylon | polyamide; PA6; PA66; moulding | Grade unspecified; PA6 and PA66 are alternative candidates |
| POM | polyoxymethylene; acetal; moulding | Grade and available proxy evidence |
| PC | polycarbonate; moulding | Resin and conversion coverage |
| ABS | acrylonitrile butadiene styrene; moulding | Resin and conversion coverage |
| Silicone | silicone rubber; elastomer; curing | Product form; do not substitute elemental silicon |
| LDPE packaging foil | LDPE film; film extrusion | Film product versus resin plus conversion |
| Cardboard packaging | cardboard; corrugated board; box conversion | Board construction, recycled content and converting coverage |
| Assembly/inspection | local electricity; assembly/quality inspection | Metered or estimated per-attempt consumption |
| Transport | freight by mode and geography | Distances, payload basis and existing upstream coverage |
| Reject/scrap treatment | appropriate waste treatment or recycling | Materials/routes, burdens, allocation and any credit |

Next, search TianGong and USLCI, inspect actual candidates and propose the primary DB and geographic scenario. No row has an accepted database supplier yet. This table must not be represented as a completed mapping table.

## 6. Interpretation at this inventory checkpoint

The production output is now more explicit: accepted goods form the denominator. Under the selected inspection stage, final-assembly rejects raise upstream component requirements and per-good-unit assembly/inspection activity, while finished packaging stays constant. A 2% reject rate increases these pre-packaging activities by approximately 2.0408%, not exactly 2%.

This does not imply an identical increase in total GWP100. Packaging, waste treatment, fabrication losses and electricity intensities still need modelling. The largest BOM mass is not necessarily the largest environmental contributor. The finished-material balance has been checked, but upstream closure, raw-material balances and characterization coverage have not.

Critical open items are grades and fabrication yields, actual baseline defect rate, quality-test/assembly energy, reject treatment, transport and dataset coverage. The original report's sheet-metal scrap default is not a final-assembly defect rate; see the source review before considering it as a yield assumption. Revisit assumptions if retrieved datasets already include losses or report inputs per good product.
