# Plains zebra: open drought behavior dataset and analysis

Species-specific secondary-analysis release, prepared 22 November 2026. This is a curated subset/derivative of existing open research, **not a newly collected dataset or a validated disaster-warning system**. Original researchers retain credit for field data. The manuscripts are exploratory and not peer reviewed.

## Dataset at a glance

| Property | Value |
|---|---|
| Animals in source subset | 6 |
| Analytical units | 6 |
| Source rows | 396 |
| Analysis rows | 396 |
| Dates | 2019-07-01 to 2020-02-29 |
| Outcome | daily GPS-derived distance (km/day) |
| Exposure | Not supplied: observed CD/HD/HW seasons only |
| Complete five-stage animal sequences | 0 |

## Download and contents

- [Analysis-ready CSV](data/analysis_data.csv) and [data dictionary](DATA_DICTIONARY.md).
- [Source records](source/source_records.csv), [provenance and checksums](source/PROVENANCE.json).
- `analysis/`: statistical contrasts and coefficients, validation splits, held-out predictions, model metrics, metadata and the exploratory saved forest.
- `scripts/`: source preprocessing, independent species reanalysis and validation.
- [Professional PDF manuscript](paper/zebra_professional_manuscript.pdf), [editable Word manuscript](paper/zebra_professional_manuscript.docx), and scientific figures in `paper/figures/`.
- `CHECKSUMS.json`: integrity hashes for all release files except this hash manifest itself.

## Original sources and credit

Original investigators: **Vera and colleagues**. [Dataset DOI](https://doi.org/10.5061/dryad.9cnp5hr2g); [related journal paper](https://doi.org/10.1111/1365-2656.70387).

Actual input source: https://doi.org/10.5061/dryad.9cnp5hr2g

Only the daily-distance records for this species are retained. Other temperature and hourly movement files are not included in these models.

## Reproduce and verify

Use a compatible Python environment and the recorded dependency versions:

```bash
python -m pip install -r requirements.txt
python scripts/validate.py
python scripts/reproduce.py
python scripts/validate.py
```

Run from the repository root. Reanalysis writes to ignored `reproduced/`, preserving the published data and results. Validation checks source-to-analysis preprocessing, release hashes, saved prediction metrics, validation splits and, when regenerated outputs exist, agreement with published results. Loading the optional joblib artifact is unnecessary for reanalysis; only load serialized models from trusted sources with compatible library versions.

The primary statistical model uses log outcomes, unit effects and, for monthly data, calendar month and year effects. Daily herbivore contrasts compare CD/HD/HW and cannot distinguish season from drought. Monthly uncertainty includes unit/year clustering sensitivity. The original multiplicity family contains 11 primary contrasts across seven species: `analysis/multiplicity_family.csv` retains those summary p-values so separate reruns preserve the original adjustment. It does not contain other species observation data.

AI comparisons use a mean baseline, seasonal ridge and random forests, with an additional contemporaneous drought-index forest for monthly data. Group-held-out and forward-time validation are reported separately. The saved full-data forest is not evidence of out-of-sample performance; use the held-out predictions and scores.

## Five stages and limitations

Requested stages are baseline, near-before, during drought, early-after and late environmental normalization. Stages are assigned only where the observation and index rules support them. Late environmental normalization does not establish behavioral recovery.

Dryad files matched repository SHA-256. CD already denotes drought. Tmin and Tmax were identical and are excluded. Hourly table has hour-label issues and is excluded. No independent onset, baseline or late-normal labels. CD/HD/HW are not the requested five stages. Season and drought period cannot be separated in this table; there is no independent pre-drought or verified late-normal baseline.

No drought causation, earthquake prediction, five-stage classification accuracy or operational early warning is established by these analyses. Full methodology, limitations and results are in the manuscript.

## License and citation

Source-data terms: **CC0-1.0 (Dryad)**. Original repository contributions: MIT. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for scope and retained notices. Cite the original dataset and paper above when using these records; identify this repository and its commit as the secondary processing version. No new DOI is claimed.

This repository is maintained under `usman-sarwar-rajput`. Repository maintenance is not a claim of authorship of the original field study.
