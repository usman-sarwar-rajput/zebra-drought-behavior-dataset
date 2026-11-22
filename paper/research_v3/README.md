# Zebra research paper

Read `zebra_research_paper.pdf` or edit `zebra_research_paper.docx`. The manuscript follows the supplied shark paper's scientific section order, with explicit statistical and prediction extensions. No author affiliations or fieldwork claims are invented.

The `analysis/` directory contains numerical results and the new animal-deletion checks; `figures/` contains scientific plots; `source/` identifies the original deposited data. Source licensing and attribution are retained in THIRD_PARTY_NOTICES.md and licenses/.

Install requirements.txt in a suitable Python environment. Run `python scripts/reproduce.py` to refit the original primary statistics and predictive benchmarks from the source records into `reproduced/`. Run `python scripts/validate.py` to check the saved files and, when present, the reproduction. From this directory, run `python reproduce_additional_analysis.py` to regenerate this species' additional sensitivity plots and tables. This last command updates the additional results in place, not the Word papers.

Full-sample AI model files are provided for reproducibility. Their training fit is not reported as validation. Model rankings are specific to the target and split design. The manuscript is an exploratory draft requiring author review before journal submission.


[Plain-language summary PDF for all three species](Animal_Drought_Research_Simple_Summaries.pdf).
