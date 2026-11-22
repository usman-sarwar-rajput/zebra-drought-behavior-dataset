# Analysis data dictionary

Outcome: daily GPS-derived distance (km/day).

| Column | Meaning |
|---|---|
| `unit` | Analytical individual or social group. Packs/prides are the independent units for wild dogs/lions. |
| `species` | Source code EQ = plains zebra; CT = blue wildebeest. |
| `sex` | Source sex code (m/f); not included in the predictive models. |
| `date` | Observation date; monthly values use the first calendar day, not a GPS fix timestamp. |
| `phase` | CD = cool drought, HD = hot drought, HW = rainy recovery. CD is not a pre-drought baseline. |
| `outcome` | Positive behavior response; see species-specific outcome and units in README. |
| `animal` | Source animal identifier(s); semicolon-separated where social-group/month rows were combined. |
| `month` | Calendar month 1–12. |
| `year` | Calendar year. |
| `monthnum` | year * 12 + month; monthly continuity index. |
| `sin_month` | sin(2*pi*month/12), seasonal predictor. |
| `cos_month` | cos(2*pi*month/12), seasonal predictor. |

Source-table fields are retained under source/ and documented in the original README where available. Blank source fields are not imputed. The analysis table includes positive outcomes only. No missing stage is synthesized. For result tables, change_pct/low_pct/high_pct are percentage contrasts and nominal bounds; p is unadjusted and q_primary_family is BH-adjusted across the original 11 primary contrasts. Prediction columns observed/predicted use outcome units; predicted_log uses the natural logarithm. Error metrics beginning log_ are on the natural-log scale, not percentages.
