# BC1 Electric Kettle: Cradle-to-Gate GWP100

**Status: initial foreground inventory development. The user-defined production output is one conforming packaged kettle. Illustrative defect scenarios are calculated; cumulative LCI and LCIA are not calculated.** All project reports, results and documentation are written in English. Learning discussions may be in Korean.

Start with the [goal and scope definition](docs/goal-and-scope.md), [inventory development](docs/inventory.md) and [phased study plan](docs/plan.md). Interpretation accompanies every phase. See the [decision log](docs/decisions.md). Unknown values never mean zero.

For a new session, read the [handoff](HANDOFF.md) and [complete LCA and HTML report execution prompt](prompts/complete-lca-and-html-report.md). The prompt specifies the remaining work; an HTML report and full LCA pipeline have not yet been implemented. The latest [attached README instructions](docs/attached-readme-instructions.md) are preserved with the project.

## 1. Study identity and purpose

| Field | Current record |
|---|---|
| Study title | Cradle-to-gate GWP100 of one packaged BC1 1 L plastic electric kettle |
| Public student/group alias | seongheon lee (postech) |
| Repository URL | [SHlee-TDA/kettle_lca_tutorial](https://github.com/SHlee-TDA/kettle_lca_tutorial) — user-designated destination for future pushes |
| Run identifier | `bc1-independent-001`, reserved for the first calculation; not executed |
| Study start date | 2026-10-08, Asia/Seoul |
| Run type / Git tag | Independent run planned / not applicable before calculation and commit |
| Goal | Learn and apply LCA, estimate production-stage GWP100, identify major contributors, and examine the influence of background-data choices |
| Audience | Student, instructor, classmates and public repository readers |
| Comparison | The same kettle specification under alternative background-data scenarios; one primary database plus comparison scenarios |

The user agreed to the goal, factory-gate boundary and declared unit. The intended application is educational analysis and transparent model comparison. Product superiority and whole-life claims are outside this goal. Submit the actual final 40-character commit SHA after committing and pushing; do not predict this README's own future hash.

Configured Git remote URL: `https://github.com/SHlee-TDA/kettle_lca_tutorial.git`. This checkpoint documents initial foreground modelling, not a completed LCA. Publication is verified separately against the remote commit.

## 2. Product, declared unit and system boundary

**Production functional unit: provision of one conforming, fully assembled and packaged BC1 1 L electric kettle at the factory gate.** The classroom declared unit remains one packaged kettle; the model reference flow is one accepted packaged unit. The manufacturing function is provision of this conforming output, while the appliance function is heating water. No water-heating service functional unit is modelled. BC1 is a representative case rather than a named commercial product. Actual quality-test protocols remain unknown.

- [Original BOM](data/foreground/kettle-bom.csv), downloaded on 2026-10-08.
- Source: the [exercise](https://tiangong-lca-decision-lab.ecodino73.chatgpt.site/) cites the EU Electric Kettles preparatory study (2020), Task 4, Tables 4-3, 4-4 and 4-8, printed pages 26, 27 and 30. The aggregate tables have now been checked against the original report: physical PDF pages 141, 142 and 145. The Task 4 cover says May 2021, while publication text retains 2020. [Source review](docs/source-review.md).
- Finished masses: **723.00 g kettle + 137.80 g packaging = 860.80 g**. These are not purchased quantities or a complete process mass balance.
- Included product system: raw-material supply, component manufacture, assembly, packaging and associated upstream energy. Inbound transport and manufacturing-waste treatment belong within this boundary; their quantities remain unresolved.
- Excluded from the baseline: customer delivery, use, maintenance and end of life after use. Manufacturing scrap is distinct from product end of life and remains within scope.
- Verified product specifications: 1 L plastic kettle, rated input power 1,000–1,400 W, without temperature selection or keep-warm. This rating is not manufacturing electricity. Geography and target reference year remain unknown.
- Proposed cut-off rule: retain every BOM entry; justify additional exclusions individually. Preserve and disclose infrastructure already included in background datasets.

Detailed definitions and implications appear in [Goal and Scope](docs/goal-and-scope.md).

## 3. Foreground inventory and quantitative assumptions

Every finished mass below is `sourced` from the supplied [BOM](data/foreground/kettle-bom.csv), cross-checked against the original aggregate tables. Grades and conversion routes have not been verified.

| Material | Finished mass (g/unit) | Scope |
|---|---:|---|
| Stainless steel | 186.00 | Kettle |
| Brass | 20.25 | Kettle |
| Copper | 15.00 | Kettle |
| Polypropylene (PP) | 350.25 | Kettle |
| Polyvinyl chloride (PVC) | 43.50 | Kettle |
| Nylon, grade unspecified | 49.50 | Kettle |
| Polyoxymethylene (POM) | 9.75 | Kettle |
| Polycarbonate (PC) | 6.75 | Kettle |
| Acrylonitrile-butadiene-styrene (ABS) | 30.00 | Kettle |
| Silicone | 12.00 | Kettle |
| LDPE packaging foil | 6.30 | Packaging |
| Cardboard packaging | 131.50 | Packaging |

| Additional input | Value / unit | Evidence and status |
|---|---|---|
| Grades and recycled content | unknown / grade, % | Evidence needed; nylon grade is unspecified |
| Fabrication yields/losses | unknown / % | Separate from final-assembly rejection; process-specific evidence needed |
| Final-assembly reject rate | actual baseline unknown; illustrative 0%, 2%, 5% | User-approved assumptions: after assembly, before packaging, no rework |
| Conversion services | unknown / dataset reference unit | Inspect included processing burdens before adding |
| Assembly electricity | unknown / kWh/unit | Not supplied by the BOM |
| Inbound transport | unknown / t·km/unit | Distances, modes and existing coverage unresolved |
| Manufacturing scrap | unknown / kg/unit | Yield, internal recirculation and treatment unresolved |
| Prices | not applicable at present | No monetary model selected |

[Production assumptions](data/foreground/production-scenarios.json) and [scenario results](results/inventory/defect-scenarios.md) distinguish finished component demand from gross raw-material purchases. With reject rate `d`, assembly attempts per good product are `1/(1-d)`. Finished component demand scales by this factor; packaging is applied only after acceptance. No component salvage is modelled in the illustration. Waste treatment remains unresolved.

Use `kg = g / 1000`. For a simple single-pass process, purchased mass equals finished mass divided by yield; scrap equals purchased mass minus finished mass. Internal recycling needs a separate balance. Normalize each activity to the dataset's actual reference amount and unit. Avoid adding material, conversion, energy or transport burdens already included in a dataset. Future assumptions will be labelled sourced, estimated or assumed. Monetary proxies, if selected, must specify sector, currency, price year, purchaser/basic-price basis, quantity and price.

## 4. Background data and matching decisions

**No background dataset has been selected or retrieved.** Only official access documentation has been reviewed.

| Candidate | Access documentation | Required checks |
|---|---|---|
| TianGong | [Official CLI](https://github.com/tiangong-lca/cli), browser sign-in and process search/retrieval | Material/process coverage, suppliers, elementary flows, CF access, geography/year and permissions |
| USLCI | [Release downloads](https://github.com/FLCAC-admin/uslci-content/blob/dev/docs/release_info/release-downloads.md), JSON-LD or openLCA packages | Candidate 1.2026-09.0, external electricity dependencies, missing materials and flow/CF compatibility |

The [September 2026 notes](https://github.com/FLCAC-admin/uslci-content/blob/dev/docs/release_info/press-release.md#2026-fall-quarter-september-30) identify external electricity links. If Commons Merged is used, record constituent packages rather than labelling everything USLCI. Monetary proxies require a separate documented choice.

The [manifest](data/manifest.json) covers the BOM, source report, illustrative production assumptions and supplied README requirements. A complete mapping table does not yet exist. It will record each input's database/release, dataset name, UUID/version, geography/year, reference flow/amount/unit, URL, retrieval date, hash, suppliers and external dependencies. Record search queries, alternatives, selection/rejection reasons and proxies, distinguishing unit-process inventories, cumulative factors and monetary estimates.

## 5. Calculation and impact-assessment methods

The proposed full LCA calculation is `A s = f`, `g = B s`, `h = C g`: solve for process activities, aggregate elementary flows, then characterize impacts. Matrix signs and reference-flow normalization will be documented. The full LCA solver and its versions are unresolved. The initial foreground calculator uses Python 3.13.6 standard-library arithmetic and implements only the documented reject normalization.

- Provider linking: explicit supplier identifiers first; justify alternatives rather than selecting by name alone.
- Allocation/system model, recycled inputs, scrap and credits: unresolved; align with the goal and selected datasets.
- Indicator: **GWP100, kg CO2-eq per packaged kettle**, 100-year horizon; other categories optional.
- Characterization method/version/source: unknown. [FEDEFL-adapted methods](https://www.lcacommons.gov/lcia-methods-without-flows) are candidates for USLCI.
- Carbon treatment: specify fossil/biogenic and land-use treatment; do not assume all biogenic CO2 is zero.
- Flow matching: verify substance/identity, compartment, subcompartment, units and regional conditions.
- Missing suppliers and uncharacterized flows: unknown until model construction. Report explicitly; distinguish unmatched flows from those outside the selected impact category. Do not silently assign zero.

## 6. How to reproduce the analysis

Current files:

```text
README.md                          Study summary and status
docs/goal-and-scope.md              Goal, product system, unit and interpretation
docs/plan.md                        Phased learning and execution plan
docs/decisions.md                   Curated decisions
docs/sources.md                     Sources and verification limits
docs/readme-requirements.md         Unmodified supplied requirements
data/foreground/kettle-bom.csv      Original downloaded BOM
data/manifest.json                 Input provenance and SHA-256 hashes
docs/inventory.md                  Initial foreground model and interpretation
docs/source-review.md              Source BOM/specification verification
data/foreground/production-scenarios.json  Explicit illustrative assumptions
src/inventory.py                   Finished-demand normalization calculator
results/inventory/                 Generated scenario report and JSON
```

Observed OS: macOS 26.5.2. The initial foreground calculator was run with Python 3.13.6 and uses only its standard library, so no third-party installation is required. Run `python3 src/inventory.py` from the project root and open `results/inventory/defect-scenarios.md` or its JSON companion. Inputs are the BOM and production-scenarios.json; the script records their hashes and validates the model. The full LCA engine, background-data retrieval commands and dependencies remain unresolved. The [source review](docs/source-review.md) provides public PDF retrieval instructions.

Obtain the BOM through “Download BOM CSV” on the exercise page. From the project root:

```sh
cat data/manifest.json
shasum -a 256 data/foreground/kettle-bom.csv docs/readme-requirements.md
```

TianGong requires official browser login if selected; its Production profile supplies defaults. For USLCI, evaluate package downloads or API access and confirm data.gov key requirements for the chosen API route. Project configuration variable names are not yet defined. Do not document secret values. Record redistribution permissions; supply precise retrieval instructions, IDs and hashes for data that cannot be shared. Fixed dependencies, caches, manual steps and inaccessible dependencies will be documented during implementation. A random seed is not applicable at present.

## 7. Results, checks and interpretation

| Item | Status |
|---|---|
| Cumulative LCI / LCIA | not calculated — background inventory and method selection pending |
| Initial foreground scenarios | calculated for illustrative 0%, 2%, 5% final-assembly reject rates |
| GWP100 total (kg CO2-eq/unit) | not calculated |
| Complete contributions, top three and figures | not calculated |
| BOM totals | PASS: 723.00 g kettle, 137.80 g packaging, 860.80 g total |
| Finished-material normalization | PASS: incoming finished components and packaging equal good output plus rejected-assembly mass |
| Full process mass balance and background units | not calculated |
| Supplier closure and double counting | not calculated |
| Contribution sum versus total | not calculated |
| Characterization coverage/unmatched flows | not calculated |

Current interpretation: the agreed boundary supports a production-stage climate estimate for a fixed product specification. It cannot establish lifetime impacts, use efficiency or overall environmental superiority. Mass alone cannot establish a GWP100 contributor ranking. Revisit these limitations during inventory and impact assessment and distinguish partial results from a complete calculation.

## 8. Uncertainty and sensitivity

Probabilistic uncertainty is **not calculated** because distributions are unresolved. A deterministic illustration of 0%, 2% and 5% final-assembly reject rates is available; these are not measured rates or probability bounds. Further sensitivity to grades, fabrication yields, assembly power and provider choices remains pending. Monte Carlo is optional if defensible distributions become available.

Distributions/ranges, correlations, simulation method, draw count, seed, convergence and mean/median/P05/P95 are not applicable yet. If calculated, describe P05–P95 as a central 90% interval conditional on the model and distributions. Separate parameter uncertainty, provider/method scenarios and repeated-AI-run variability.

## 9. Codex and human decisions

Planning began on 2026-10-08. The displayed Codex model/version and available settings are **unknown — not directly verified**. The [decision log](docs/decisions.md) records consequential requests, choices and revisions without private messages or credentials.

The user chose one primary DB plus comparisons, GWP100 first, geography based on representativeness, English deliverables and gradual LCA phases with interpretation throughout. The user agreed to the educational goal and production boundary, then refined the output to one conforming product and chose an illustrative reject-rate model. Codex verified the original BOM and generated checked foreground scenarios. No background datasets have been accepted and no cumulative LCI or LCIA results exist. Independent human verification of calculations is pending.

## 10. Independent and revised runs

No independent cumulative LCI or LCIA result exists. The illustrative foreground scenarios are stored separately in `results/inventory/`. Preserve inputs, settings, results and checks for the later `bc1-independent-001` run and record its actual tag/commit before reviewing classmates' results.

Revised runs are **not applicable — none performed**. A later revision will record the prior commit, one changed decision, predicted effect, original/revised results, absolute/percentage differences and explanation. Percentage change is undefined if the original is zero. Distinguish error corrections from defensible alternatives. A complete DB substitution may change multiple conditions and must be distinguished from a single-choice experiment.
