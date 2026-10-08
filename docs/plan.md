# Study Plan

Date: 2026-10-08 (Asia/Seoul). All deliverables are in English. Proceed gradually, explaining each LCA phase before the next. Interpretation accompanies each phase and may lead to documented revisions.

## Current phase

The user has refined the production output to one conforming packaged kettle and authorized inventory work. [Initial inventory development](inventory.md) now includes verified BOM sources and a reproducible illustration of final-assembly rejects. Background-data matching and cumulative LCI are pending; characterization has not begun. Detailed scope choices remain unresolved.

## Phases and interpretation

| Phase | Work | Interpretation |
|---|---|---|
| 1. Goal and scope | Define purpose, audience, system, boundary and unit; identify open scope choices | Check that the proposed result answers the question; explain excluded conclusions |
| 2. Inventory analysis | Check source BOM; search both DBs; propose geography/primary DB; specify manufacturing inputs and link upstream providers | Check completeness, representativeness, units, balances, proxies and double counting; revise scope if necessary |
| 3. Impact assessment | Select a traceable GWP100 method/version; classify and match flows; characterize; report total and contributions | Assess factor coverage, dominant contributors, sensitivity and supported conclusions |
| 4. Synthesis and comparison | Preserve independent results; compare data scenarios; make a separate single-choice revision | Separate data, geography and method effects; explain robustness and limitations |
| 5. Publication and submission | Verify reproduction, complete README, publish to GitHub and submit the exact commit | Ensure claims fit the goal and the submitted version is retrievable |

At each transition, explain the findings and discuss consequential unresolved choices with the user. Do not bundle unfamiliar assumptions into an unexplained calculation.

## Agreed preferences and open choices

Agreed: one primary DB plus comparison scenarios; GWP100 first; optional other categories; representative geography to be proposed; English deliverables; step-by-step discussion; interpretation throughout; production-stage study per packaged kettle.

Open: geography/year, DB/release, material grades/proxies, yields, assembly energy, transport, allocation/scrap, CF version and solver. Resolve these at the relevant phase with evidence, not invented defaults.

## Later data selection

Evaluate coverage of all 12 materials and required processing, upstream closure, technology/geography/year, characterization compatibility and reproducibility. Inspect difficult matches such as nylon, silicone, POM and PC. Distinguish TianGong CLI software versions from dataset versions. USLCI 1.2026-09.0 is a candidate only; record external Commons dependencies. Monetary proxies require a rationale and price metadata.

## Later implementation

The user now requests a reproducible calculation pipeline that automatically generates an English HTML report from its actual results, alongside README and detailed data. See the [execution prompt](../prompts/complete-lca-and-html-report.md) and [handoff](../HANDOFF.md). This pipeline is not yet implemented. Choose software after inspecting data; use a tested LCA engine when needed to preserve allocation, formulas and waste-flow semantics. An offline HTML report is sufficient; hosting and a dashboard are not required.

Check BOM totals, units, reference amounts, balances, providers, CF matching, contribution sums, matrix residuals and double counting. Preserve unknowns and distinguish partial from complete results.

## Comparison and preservation

Maintain the unit, foreground quantities, boundary and, where feasible, the same CF method/version. Begin with corresponding processes, then build labelled product scenarios. A partial substitution is not a complete second-DB model. Discuss geography, technology, allocation and method differences before attributing differences to a database.

Future outputs may include a mapping table, foreground assumptions, code and separate `bc1-independent-001`, `bc1-scenario-001` and `bc1-revised-001` run folders. These do not exist yet. Preserve the independent result before class comparison. Record predictions before changed-choice calculations.

## User input at the relevant phase

- During inventory: geography, important proxies and weakly evidenced assumptions; predicted major contributor before calculation.
- Before characterization: explain and select the method and its limitations.
- Before publication: review final documents and verify the designated repository. Public identity: seongheon lee (postech). Push destination: `https://github.com/SHlee-TDA/kettle_lca_tutorial.git`.
- At submission: handle required name, email and submission code in the form, not public files.
