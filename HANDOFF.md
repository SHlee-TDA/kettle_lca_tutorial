# Handoff: BC1 Kettle LCA

Recorded: 2026-10-08 (Asia/Seoul). This handoff prepares a new session; it does not assert completion of the LCA.

## Start here

Read and execute [the full new-session prompt](prompts/complete-lca-and-html-report.md). It requests actual LCA execution, interpretation-driven iteration and automatic HTML report generation. The new [attached README instruction](docs/attached-readme-instructions.md) is preserved verbatim; the earlier [checklist](docs/readme-requirements.md) also remains available.

## Repository checkpoint

- Repository: https://github.com/SHlee-TDA/kettle_lca_tutorial
- Origin: `https://github.com/SHlee-TDA/kettle_lca_tutorial.git`; working branch: `main`.
- Initial project checkpoint: `a5309f008c1634a4181f470057b00aaaa1e07071`, successfully pushed on 2026-10-08. This is a preparation/foreground checkpoint, **not a completed independent LCA**.
- The handoff and prompt are added in a subsequent commit. Obtain its actual SHA from Git rather than interpreting the checkpoint above as the latest version.
- Normal Git HTTPS push worked with existing credentials. GitHub CLI was not signed in; `gh` authentication is not a prerequisite if ordinary Git continues to work.
- Public alias: **seongheon lee (postech)**, explicitly selected by the user. Commits use the public GitHub no-reply address rather than a private email.

## Completed and verified

- English README with all ten required sections, goal/scope, plan, decision log and source review.
- Source BOM preserved exactly: 12 materials, 723.00 g kettle, 137.80 g packaging, 860.80 g total.
- Original report aggregate tables visually/textually checked: Task 4 printed pp. 26/27/30, physical PDF pp. 141/142/145. Manufacturing note checked at PDF p. 166.
- A standard-library Python calculator for finished-component demand under illustrative 0%, 2% and 5% final-assembly rejection.
- Tests/checks cover BOM totals, invalid reject rates, a known batch example and finished-material balance. These do not prove upstream supplier closure or a full factory material balance.
- Input hashes, local document links and English documentation checked.

## Not completed

**No accepted background dataset, complete purchased-input inventory, cumulative elementary-flow inventory, characterization factors, GWP100 result or HTML report exists.** No course submission has been made. The user initially believed the procedures were complete; the actual repository status was clarified before publication. Keep these gaps visible.

## Decisions to preserve

- Educational cradle-to-gate study, one conforming assembled and packaged BC1 1 L kettle at the factory gate. Retain the classroom declared unit alongside the production functional-unit wording.
- Include raw materials, manufacturing, assembly, packaging, upstream energy, inbound transport and manufacturing waste; exclude consumer use and post-use end of life.
- One primary DB, TianGong or USLCI, plus a comparison scenario from the other. GWP100 first.
- Geography/year and method version are unresolved; propose them using evidence.
- Inspection after assembly and before packaging; no rework. Scenario rates 0/2/5% are illustrative, not a baseline. No salvage and complete-BOM rejects are documented model simplifications, not observed factory facts.
- Explain consequential decisions in Korean; write all deliverables in English. Interpret at each phase and iteratively update any affected earlier phase.

## Files and reproduction

| File | Role |
|---|---|
| `docs/goal-and-scope.md` | Agreed question, boundary and refined production unit |
| `docs/inventory.md` | Equations, assumptions, candidate search worklist and interpretation |
| `data/foreground/kettle-bom.csv` | Original finished-mass BOM; preserve CRLF bytes/hash |
| `data/foreground/production-scenarios.json` | Explicit illustrative assumptions; unknown inputs are null |
| `src/inventory.py` | Partial normalization calculator; not an LCA solver |
| `results/inventory/defect-scenarios.json` | Detailed scenario values and input hashes |
| `results/inventory/defect-scenarios.md` | Generated English foreground report |
| `data/manifest.json` | Source/assumption provenance and hashes |
| `docs/source-review.md` | Source verification, date distinctions and download instructions |
| `docs/decisions.md` | Human choices versus model simplifications |

From the repository root:

```sh
python3 src/inventory.py
git status --short
git remote -v
```

Last verified environment: macOS 26.5.2, Python 3.13.6, standard library only. On another Python version the generated JSON's recorded version may change. Inspect generated diffs rather than assuming bitwise identity across environments.

The source PDF cache is deliberately excluded from Git. A fresh clone will not contain `data/cache/kettle-preparatory-study.pdf`; its manifest entry is provenance, not a missing tracked deliverable. Retrieve it only when needed using `docs/source-review.md` and verify its hash. All currently tracked inputs needed for the illustrative calculator are supplied.

## Important interpretation traps

- At 2% rejects, 737.7551 g is finished kettle-component demand per good unit, not gross material purchases; packaging remains 137.8000 g under the specified inspection placement. Rejected assembly mass is 14.7551 g. No GWP100 follows from these masses alone.
- Fabrication loss and final-assembly rejection are separate. Dataset loss factors or good-product normalization may already include relevant burdens.
- The report's 25% sheet-metal scrap default is not a kettle defect rate. Its denominator and applicability are unverified for this model.
- The Task 4 cover says May 2021; publication/copyright text says 2020; PDF compilation metadata says September 2022. None establishes all dataset measurement years.
- Source rated power of 1,000–1,400 W is an operating specification, not assembly electricity.
- TianGong CLI version is not a database release. USLCI 1.2026-09.0 was only a candidate; its external electricity dependencies need explicit closure. Recheck current official docs when resuming.
- Missing providers/CFs are unknown, not zero. A numerical solver success does not prove model completeness.

## Next actions

1. Audit files and rerun the partial calculator.
2. Start the interpretation/iteration log and explain the unresolved choices without reopening settled decisions unnecessarily.
3. Check DB access, search candidate providers and CFs, propose geography/primary DB, and obtain essential modelling decisions.
4. Complete LCI, characterization, interpretation and comparison with provenance and checks.
5. Implement automatic HTML generation from actual machine-readable results, verify it, update README and publish as directed in the execution prompt.

The HTML pipeline is future work. No command claimed to generate a full LCA HTML report exists at this checkpoint.
