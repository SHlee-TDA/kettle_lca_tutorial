# Source Review: BC1 Specification and BOM

Reviewed on 2026-10-08. Source: *Preparatory study for Kettles implementing the Ecodesign Working Plan 2016-2019*, combined report hosted by Fraunhofer. [Download](https://publica-rest.fraunhofer.de/server/api/core/bitstreams/3df3f4d6-3717-4261-99e3-a232323111d6/content).

The unmodified 305-page PDF is cached locally as `data/cache/kettle-preparatory-study.pdf` and excluded from Git. Its SHA-256 is `413980bdfdd02e05bd10e13b507b298bddc99f527adc207e8f7c6e8898532152`. To retrieve it from the project root:

```sh
mkdir -p data/cache
curl -fL --max-time 600 https://publica-rest.fraunhofer.de/server/api/core/bitstreams/3df3f4d6-3717-4261-99e3-a232323111d6/content -o data/cache/kettle-preparatory-study.pdf
shasum -a 256 data/cache/kettle-preparatory-study.pdf
```

A first download timed out; resuming the same public file succeeded. A partial transfer must not be accepted without a successful completion and hash check.

## Document dating

The exercise labels the study 2020. The Task 4 cover in the linked combined PDF says May 2021, while its publication/copyright material retains 2020. PDF metadata records compilation in September 2022. Record these distinct dates rather than treating the PDF creation date as the BOM measurement year. A unique underlying measurement year is not established by this review.

## Verified source facts

The BC1 columns in Task 4 Tables 4-3, 4-4 and 4-8 were checked using text extraction and rendered page images. Printed pages 26, 27 and 30 correspond to physical PDF pages 141, 142 and 145.

- The 12 classroom BOM quantities match the corresponding source entries. The kettle total is 723.00 g; packaging is 6.30 g LDPE foil plus 131.50 g paper/cardboard packaging, giving 860.80 g packaged mass.
- BC1 is a simple plastic kettle with 1.0 L capacity, rated input power of 1,000–1,400 W, without temperature selection or keep-warm. Rated operating power is a product characteristic, not assembly electricity consumption.
- Task 4 section 4.2 describes the base cases as representative models informed by existing product data. Its BOM derivation cites dismantling work by Gallego-Schmid et al. (2018). That underlying paper has not been independently verified here.
- The source lists nylon without establishing PA6 versus PA66. Manufacturing geography and a measured final-assembly reject rate were not established by the inspected sections.

## Manufacturing clue requiring further interpretation

Task 5 section 5.1.6.1, printed page 15 (physical PDF page 166), reports the use of EcoReport's mass-based component-manufacturing impacts and identifies 25% as its default sheet-metal scrap parameter. This is not a measured BC1 final-assembly defect rate. The denominator, process coverage and whether equivalent losses are already included in a candidate background dataset must be checked before converting it into an inventory yield. It is a candidate source assumption, not an adopted input to the current calculator.

The present study will construct its own traceable model using the selected LCI database. EcoReport's manufacturing impacts will not be added on top of equivalent background conversion burdens.

## Interpretation

The supplied BOM is supported by the original aggregate tables. It remains a finished-mass specification for a representative product, not a measured factory input inventory. Converting it into a production inventory still requires explicit grade, yield, quality-rejection, energy, transport and waste-treatment decisions.
