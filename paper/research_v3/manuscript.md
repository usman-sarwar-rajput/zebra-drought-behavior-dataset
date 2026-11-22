# Movement differences across drought and rainy recovery in plains zebra

A retrospective observational study following the supplied shark paper structure

Full manuscript version 3 | 22 November 2026 | Exploratory secondary analysis

## Abstract

Objective: How does measured daily movement differ between the observed cool-drought, hot-drought and rainy-recovery windows, and can seasonal models predict those records? Data: 6 animal identifiers contributed 396 source observations; the final analysis used 396 records from 6 analytical units. Methods: separate log-scale statistical models and fixed-parameter random forests were evaluated with explicit seasonal controls, group-held-out validation and forward-time validation. An independent coverage screen assessed baseline, near-before, during, early-after and late environmental normalization. Results: The rainy-recovery versus hot-drought contrast was +36.5% in modelled daily movement, with a nominal interval of +15.9% to +60.7% and q = 0.017. The strict five-stage screen identified 0 complete animal-level sequences. The lowest log-MAE on unseen units was 0.523; the lowest later-period log-MAE was 0.498. These rankings are descriptive validation results, not tests of model superiority. Conclusion: Daily movement differs clearly between the observed periods under the specified model, but drought progression and season are inseparable. These results do not supply a genuine pre-drought baseline or a validated late-normal stage. Neither predictive performance nor a period contrast alone establishes drought causation or disaster anticipation.

Individual-deletion fits and paired-animal descriptions supplement the primary model to expose sensitivity to uneven coverage and very low movement records.

Keywords: Equus quagga; drought; animal movement; home range; seasonal confounding; random forest; grouped validation

## 1 Introduction

The supplied shark manuscript [7] provides the organizational reference: abstract, introduction, related research, methodology, results, discussion, conclusion and data availability. Its single-animal hurricane comparison is descriptive and contains no fitted statistical or AI model. We transfer its explicit period comparisons, but add separately documented statistical and prediction analyses. The reference does not justify copying shark-specific depth outcomes or hourly windows into terrestrial movement data.

The supported descriptive sequence contains three observed periods: cool drought, hot drought and rainy recovery. A verified pre-drought and late-normal period are absent. This paper therefore follows the reference structure with three factual periods, rather than manufacturing five labels. The phase names describe the deposited data and are not independently inferred from the movement outcomes.

This study examines records for the plains zebra using openly deposited observations from Etosha National Park Namibia. Its purpose is to determine what the available records can support, rather than assume that every apparent temporal change is a response to a disaster. The scientific object is a recorded behavioral measure, not a direct measure of physiological stress, survival, motivation or disaster perception. Those distinctions constrain the interpretation of every subsequent result.

A five-stage framework can be useful for organizing questions about onset and recovery. It can also create misleading certainty if stages are assigned from a calendar alone or if the same outcome is used to define recovery and then test it. Here, candidate drought onsets are defined from environmental exposure, while calendar-stage completeness and stricter environmental recovery are evaluated separately. A missing stage remains missing. Repeated rows from one animal or one shared climate event are not interpreted as independent replications.

Three questions guide the analysis. First, how much behavioral variation is associated with observed dryness or the available period labels after the controls supported by the data? Second, do nonlinear models predict held-out observations better than simple baselines? Third, does the sampling structure permit all five requested stages to be compared? These questions have different targets. A model that predicts behavior can succeed without identifying a causal drought effect, and a dataset can show period differences without supporting an advance-warning system.

## 2 Related research and study context

The source herbivore study records movement and physiological information across drought and rainy recovery [1, 2]. This manuscript uses the daily-distance table. It does not substitute temperature anomalies for movement, reconstruct original GPS tracks, or assume that cool drought is an untreated baseline. The same seasonal progression generates both phase and calendar timing, so the data alone cannot disentangle these influences.

Random forests provide a nonlinear comparison [3], while blocked validation is appropriate to the dependence questions raised by ecological records [4]. Multiple primary comparisons are summarized using the Benjamini-Hochberg adjustment [5]. These references motivate methods; they do not turn this observational design into a randomized experiment. The literature coverage is focused on source data and methods and is not claimed to be a systematic review.

## 3 Methodology

### 3 1 Provenance and analysis units

Dryad files matched repository SHA-256. CD already denotes drought. Tmin and Tmax were identical and are excluded. Hourly table has hour-label issues and is excluded. The original records were retained. Counts in the analysis table were verified against source rows, unit identifiers and dates. Results apply to the specified downloaded version; an authentic file hash establishes file identity, not the biological correctness of every value.

CD is already a drought period. HD and HW occur in different calendar months from CD, and the daily-distance table has no independent continuous drought covariate. Only six individuals support animal-clustered uncertainty. The source maximum and minimum temperature files are byte-identical, and hourly movement labels include issues, so those outcomes are not silently substituted into this analysis.

Table 1 Data and observation scope



| Property | Value |
| --- | --- |
| Species | Plains zebra (Equus quagga) |
| Animal identifiers | 6 |
| Analysis units | 6 |
| Source observations | 396 |
| Final records | 396 |
| First and last observation | 2019-07-01 to 2020-02-29 |
| Outcome | daily GPS-derived distance (km/day) |
| Exposure | Not supplied: observed CD/HD/HW seasons only |

Figure 1. Species-specific workflow. Source observations, analytical units and temporal designs are different counts. Elephant calendar and strict recovery sequences are separate; herbivores retain their three observed periods.

![Figure 1. Species-specific workflow. Source observations, analytical units and temporal designs are different counts. Elephant calendar and strict recovery sequences are separate; herbivores retain their three observed periods.](figures/01_workflow.png)

### 3 2 Quality checks and exclusions

The analysis checks positive outcomes before applying logarithms and verifies that unit-date keys are unique after the stated preprocessing. Missing times are not interpolated. Invalid model support is reported rather than filled with synthetic animals or stages. Continuous values are not rounded before fitting. The response definition is retained consistently within each species.

The minimum and maximum temperature files in the source deposit are identical, and the hourly movement file contains hour values outside its stated coding convention. Those tables are not used to generate a larger nominal sample for this study. The daily-distance table has no negative or missing response values in the present analysis. Extreme values are retained in the primary analysis and individual influence is examined in sensitivity fits; the derived table alone cannot establish whether an extreme observation is erroneous.

### 3 3 Descriptive distribution

Table 2 Distribution of the analyzed response



| Statistic | Value |
| --- | --- |
| Minimum | 0.311 |
| First quartile | 7.760 |
| Median | 12.552 |
| Mean | 14.765 |
| Third quartile | 18.459 |
| Maximum | 311.482 |
| Records per unit minimum and maximum | 58 and 85 |

These are pooled descriptive statistics, not independent observations or adjusted population estimates. The mean can be strongly affected by a small number of large ranges, while relative comparisons can be affected by small baseline values. Unit-balanced predictive errors and log-scale models address different parts of that issue; neither replaces a raw-fix audit.

Figure 2. Observed response records and exposure support. The response is displayed on a log scale. No line or histogram implies observations in unrecorded periods. The threshold line in monthly studies marks the selected three-month definition only.

![Figure 2. Observed response records and exposure support. The response is displayed on a log scale. No line or histogram implies observations in unrecorded periods. The threshold line in monthly studies marks the selected three-month definition only.](figures/02_data_support.png)

### 3 4 Observed periods and eligibility

The three period labels supplied by the dataset are retained without inferring exposure from movement. CD denotes cool drought in July 2019, HD denotes hot drought in November 2019, and HW denotes hot wet conditions during rainy recovery in February 2020 [1, 2]. All three periods are part of a drought-to-rain seasonal progression. None is a verified non-drought baseline.

Table 3 Observed period definitions



| Period | Meaning | Interpretive limit |
| --- | --- | --- |
| CD | Cool drought in July 2019 | Drought already occurring |
| HD | Hot drought in November 2019 | Season and drought cannot be separated |
| HW | Hot wet rainy recovery in February 2020 | Normal movement is not independently established |

Exact dates and animal-day coverage are taken from the deposited daily table and reported in Table S1. Different animals have different phase coverage, and unrecorded dates are not interpolated. Animals need at least one positive daily-distance record to contribute to an observed period; paired descriptions require observations in both named periods. A five-stage baseline-to-recovery analysis is unavailable because independent pre-drought and late-normal observations are absent.

Figure 3. Actual sampling support in the three observed periods. Animals and animal-days are different measures of replication. CD is already drought, and HW is a rainy period rather than evidence of normal behavior.

![Figure 3. Actual sampling support in the three observed periods. Animals and animal-days are different measures of replication. CD is already drought, and HW is a rainy period rather than evidence of normal behavior.](figures/06_five_stage_coverage.png)

Period descriptions first average days within each animal and then average the available animals equally. Paired arithmetic comparisons retain the same animals on both sides of a contrast. The fitted log-scale model uses its full observed sample and therefore targets a different average. Reporting all three summaries prevents changing animal composition or transformation from being mistaken for a biological contradiction.

### 3 5 Statistical methodology

#### Model target and specification

Equation: log Y(i,t) = α(i) + β(HD) I(HD) + β(HW) I(HW) + ε(i,t)

Y is positive daily distance and the reference period is CD. The three contrasts are HD versus CD, HW versus CD, and HW versus HD. The last contrast is the difference between the two fitted period coefficients on the log scale. The exponentiated coefficient compares modelled geometric levels; it need not equal the percentage difference between arithmetic phase means. Unit effects account for stable individual differences, but do not separate phase from calendar season.

A separate calendar-month effect cannot solve the main confounding problem when the observed phases occupy distinct selected months. Including redundant labels would not create new information. The inference is therefore explicitly about the observed windows. A low conditional p-value is not evidence that dryness, rather than the season or another shared process, caused the difference.

#### Estimation dependence and uncertainty

Reported nominal intervals are two-sided 95% t intervals. The design matrix is checked for rank. Pivoted QR removes only redundant nuisance columns while retaining the exposure contrast, and least-squares coefficients are independently recomputed for validation. The full fitted coefficient vectors are exported. No hierarchical random-effects model or causal identification strategy is claimed when neither was fitted.

The daily-window model clusters by animal and uses animal count minus one reference degrees of freedom. Repeated records within an animal are not treated as independent for this uncertainty calculation. However, clustering by animal does not create independent drought episodes. The common observed seasonal progression remains a shared exposure and is the principal reason not to make a drought-specific causal claim.

#### Multiplicity and robustness

The primary family consists of 11 contrasts across the seven separate species studies: one continuous contrast for each monthly species and three window contrasts for each herbivore. Benjamini-Hochberg adjusted values are reported for that family [5]. Sensitivities are labelled separately. The adjustment does not correct every exploratory decision, guarantee independence or resolve confounding. In this manuscript, adjusted values describe the completed analysis rather than a preregistered confirmatory test.

An uncertainty band that includes no change is not proof of no biological effect. Conversely, a band that excludes no change is not sufficient for causal attribution. We consider exposure support, model dependence, sample composition and out-of-sample performance alongside the interval. When all five stages cannot be identified, a formal five-stage contrast is withheld instead of using an arbitrary replacement baseline.

### 3 6 Machine learning and validation

#### Separate models and predictors

A fixed-parameter random-forest regressor predicts log behavior [3]. It uses 120 trees, maximum depth five, a minimum leaf size equal to the larger of three observations and the integer part of three percent of training rows, and random seed 20261122. No hyperparameter search is conducted on the test results. The final full-data model is saved for reproducibility; its in-sample fit is not used as the reported performance.

Season is encoded by sine and cosine of calendar month. The seasonal ridge baseline standardizes its predictors inside each training fold and uses penalty alpha equal to one. A seasonal forest uses the same cyclic predictors. Monthly studies also fit a forest with the negative three-month index. This additional predictor is contemporaneous environmental information. Animal identifiers, outcome-derived phase labels, future behavior and record-specific target summaries are not predictive features.

The mean baseline predicts the training mean of the log outcome. On the original scale this corresponds to a geometric mean, not an arithmetic mean. Forest and ridge predictions are also exponentiated without a smearing correction. Consequently, original-scale predictions should not be interpreted as unbiased conditional arithmetic means. Raw-scale error is nevertheless reported as an additional practical diagnostic.

Table 4 Prediction targets and model settings



| Component | Specification |
| --- | --- |
| Target | Natural logarithm of daily GPS-derived distance |
| Seasonal features | Sine and cosine of calendar month |
| Environmental feature | None available in the daily movement table |
| Random forest | 120 trees; depth 5; minimum leaf max of 3 and 3 percent of training rows |
| Ridge baseline | Training-fold standardization; alpha 1 |
| Excluded features | Animal ID; future outcomes; target-derived summaries |
| Five-stage classifier | Not validated or supplied because independent stage/event support is inadequate |

#### Held out units and later periods

GroupKFold uses up to five folds and keeps every record from a held-out animal or social unit outside that fold's training set [4, 6]. This evaluates transfer to new units within the observed data environment. It does not ensure a new climate event, because training and test units can share calendar periods. Group splits are audited for zero overlap in unit membership.

Forward validation uses expanding earlier observations and later test blocks. Monthly datasets divide observed unique dates into four blocks and apply a 31-day gap between the last eligible training date and the test start. Daily herbivore datasets use their observed calendar-month windows and a seven-day gap. Folds with fewer than eight training rows or fewer than two test rows are skipped. Animals can appear in both training and future test periods; that question differs from unseen-animal transfer.

This is a later-period prediction test with climate information observed in the target period, not a prospective forecast using only information available before drought. The temporal gap reduces immediate overlap but cannot remove every environmental dependence. Test observations are never used to fit standardization or choose settings. A stronger deployment claim would need an independent, untouched drought event and predictors available at the intended warning time.

#### Evaluation metrics

Equation: Log MAE = (1 / n) Σ | log Y − predicted log Y |

Log mean absolute error is the primary ranking measure. Lower values indicate smaller log-scale prediction errors; they are not accuracy percentages. Log root-mean-square error emphasizes larger log errors. Raw mean absolute error expresses the difference after back-transformation in the response's units. Unit-balanced log-MAE first averages absolute log error within each test unit and then averages units equally, reducing dominance by long-observed units. These metrics can rank models differently and are therefore all retained.

A test-set winner is not automatically statistically superior. We do not report a significance test of small performance differences or a tuned universal best model. Incremental value of dryness is assessed by comparing the climate forest with the seasonal forest on the same folds, while the mean and ridge baselines show whether additional complexity helps at all. Negative improvements are reported rather than hidden.

### 3 7 Individual influence and reproducibility checks

The full primary regression is refitted and its coefficient, uncertainty interval and p-value are compared numerically with the retained analysis. Next, every animal is omitted once and the same primary specification is refitted to the remaining observations. The range of estimates is a deterministic influence diagnostic, not a confidence interval. No animal is automatically rejected as erroneous. The original eleven-contrast multiplicity family remains fixed; choosing three papers does not reduce that family after results are known.

For each pair of observed periods, daily observations are first averaged within animal. The same animals then contribute to both period means. Counts increasing or decreasing show directional heterogeneity without assuming independent days. These are descriptive paired comparisons, with no added significance test. They expose differences between arithmetic and geometric estimands and between balanced and changing samples.

Every saved prediction score is recalculated from out-of-sample observed values and predicted logarithms. Model settings are retained rather than tuned to the present manuscripts. Primary model refits, animal-deletion fits, paired tables and source hashes are included in the research package. New robustness results are explicitly separated from the existing primary regression and AI benchmarks.

## 4 Results

### 4 1 Statistical associations

Table 5 Statistical estimates and uncertainty



| Model and contrast | Change | 95% nominal interval | p | Adjusted q |
| --- | --- | --- | --- | --- |
| primary
HD vs CD | +45.9% | +21.4% to +75.5% | 0.0033 | 0.0165 |
| primary
HW vs CD | +99.2% | +60.1% to +147.7% | 0.0005 | 0.0051 |
| primary
HW vs HD | +36.5% | +15.9% to +60.7% | 0.0045 | 0.0165 |

The rainy-recovery versus hot-drought contrast was +36.5% in modelled daily movement, with a nominal interval of +15.9% to +60.7% and q = 0.017.

The contrasts apply to the selected daily windows rather than continuous monitoring through every intervening day. Individuals have unequal phase coverage. The fixed-effect estimates pool the information supported by the model, so they differ from a simple paired arithmetic mean restricted to animals observed in two particular phases. These distinct summaries should not be presented as contradictory or interchangeable.

Figure 4. Separate statistical estimates on a multiplicative ratio axis. A ratio of one denotes no modeled change. Monthly comparisons are per one-unit drier exposure; herbivore comparisons are between the named windows. Bands are nominal model-dependent uncertainty.

![Figure 4. Separate statistical estimates on a multiplicative ratio axis. A ratio of one denotes no modeled change. Monthly comparisons are per one-unit drier exposure; herbivore comparisons are between the named windows. Bands are nominal model-dependent uncertainty.](figures/03_statistics.png)

The fitted period contrasts use a geometric response scale and all observations supported by the model. They are not raw arithmetic changes for an identical pairwise-complete subset. Where a large relative change is driven by very small baseline values, its numerical size warrants scrutiny before biological interpretation.

### 4 2 Out of sample predictive results

Table 6 Unseen units predictive performance



| Model | Rows | Log MAE | Unit balanced | Log RMSE | Raw MAE |
| --- | --- | --- | --- | --- | --- |
| mean | 396 | 0.533 | 0.531 | 0.687 | 7.26 |
| seasonal forest | 396 | 0.523 | 0.523 | 0.682 | 7.15 |
| seasonal ridge | 396 | 0.525 | 0.524 | 0.684 | 7.16 |

For unseen units, seasonal forest has the lowest observed pooled log-MAE, 0.523. Its raw MAE is 7.15 km/day. This ranking applies only to this species, metric and validation design. It is not a cross-species ranking of biological predictability.

Table 7 Later periods predictive performance



| Model | Rows | Log MAE | Unit balanced | Log RMSE | Raw MAE |
| --- | --- | --- | --- | --- | --- |
| mean | 303 | 0.519 | 0.540 | 0.653 | 7.63 |
| seasonal forest | 303 | 0.498 | 0.521 | 0.636 | 7.39 |
| seasonal ridge | 303 | 0.510 | 0.532 | 0.646 | 7.53 |

For later periods, seasonal forest has the lowest observed pooled log-MAE, 0.498. Its raw MAE is 7.39 km/day. This ranking applies only to this species, metric and validation design. It is not a cross-species ranking of biological predictability.

Figure 5. Predictive error on held-out units and later periods. The same metric is used within each panel. Simple baselines remain part of the comparison, and a smaller bar does not establish a significant superiority claim.

![Figure 5. Predictive error on held-out units and later periods. The same metric is used within each panel. Simple baselines remain part of the comparison, and a smaller bar does not establish a significant superiority claim.](figures/04_model_comparison.png)

The daily-distance table supplies no independent continuous drought feature. The forest is therefore a seasonal behavioral benchmark. Calling it a drought classifier would misrepresent its inputs and validation. Any apparent success can arise from regularities associated with the observed calendar windows rather than detection of an impending environmental disaster.

Figure 6. Held-out random-forest predictions versus observations on log axes. The dashed line is equality. Monthly panels show the season-and-drought forest; daily panels show the seasonal forest. Every point is from a test fold, not the final model's training fit.

![Figure 6. Held-out random-forest predictions versus observations on log axes. The dashed line is equality. Monthly panels show the season-and-drought forest; daily panels show the seasonal forest. Every point is from a test fold, not the final model's training fit.](figures/05_prediction_diagnostics.png)

Prediction plots help reveal shrinkage toward common values and errors at the extremes. A model can have a modest average error yet miss unusually large ranges or unusually low movement. The data do not establish calibrated prediction intervals, individual welfare thresholds or an operational alarm. These tasks would require separate models, labels and external evaluation.

### 4 3 Strict recovery stage sensitivity

No complete five-stage sequence meets the stated eligibility rule. The absence is an observed design limitation. A diagram with five headings would not repair it, and training a classifier on invented or calendar-derived stages would not demonstrate animal sensing of drought. The paper therefore reports the supported continuous or period comparison, preserves partial information where present, and withholds an unsupported five-stage effect.

### 4 4 Reference style temporal comparisons

Table S1 Observed periods and animal balanced movement



| Period | Animals | Animal days | Observed dates | Mean km per day |
| --- | --- | --- | --- | --- |
| CD | 3 | 93 | 2019-07-01 to 2019-07-31 | 11.84 |
| HD | 6 | 180 | 2019-11-01 to 2019-11-30 | 14.91 |
| HW | 5 | 123 | 2020-02-01 to 2020-02-29 | 17.26 |

Table S2 Paired animal arithmetic comparisons



| Contrast | Paired animals | Change | Increased | Decreased |
| --- | --- | --- | --- | --- |
| HD vs CD | 3 | +37.4% | 3 | 0 |
| HW vs CD | 2 | +50.5% | 2 | 0 |
| HW vs HD | 5 | +14.5% | 4 | 1 |

Across available animals, arithmetic daily-distance means are 11.84, 14.91 and 17.26 km/day for CD, HD and HW. Restricting each contrast to animals observed in both phases yields increases of 37.4%, 50.5% and 14.5%, respectively. The CD-to-HW paired comparison contains only two animals. Four of five animals increase between HD and HW, while one decreases. The larger fixed-effect log-scale changes in Table 5 are not the same estimand as these arithmetic changes.

Figure S1. Reference-style observed period comparison. Elephant trajectories use complete calendar sequences with equal animal weight; herbivore trajectories show actual animal means for three phases. Missing data are not filled. A later or rainy period does not prove restoration of normal movement.

![Figure S1. Reference-style observed period comparison. Elephant trajectories use complete calendar sequences with equal animal weight; herbivore trajectories show actual animal means for three phases. Missing data are not filled. A later or rainy period does not prove restoration of normal movement.](figures/08_observed_periods.png)

### 4 5 Individual animal sensitivity

Table S3 Range of estimates when each animal is omitted once



| Contrast | Minimum change | Maximum change | Fits |
| --- | --- | --- | --- |
| HD vs CD | +35.0% | +53.2% | 6 |
| HW vs CD | +87.0% | +112.4% | 6 |
| HW vs HD | +30.0% | +42.4% | 6 |

Every one of the six animal-deletion fits retains a positive coefficient for each period contrast. Estimated changes range from 35.0% to 53.2% for HD versus CD, 87.0% to 112.4% for HW versus CD and 30.0% to 42.4% for HW versus HD. This supports directional stability within this model and sample. It does not remove seasonal confounding or show that every individual responds identically.

Figure S2. Leave-one-animal-out primary regression estimates. Each point omits one animal; the black diamond is the full-sample estimate. The spread is an influence diagnostic, not a sampling interval or independent replication.

![Figure S2. Leave-one-animal-out primary regression estimates. Each point omits one animal; the black diamond is the full-sample estimate. The spread is an influence diagnostic, not a sampling interval or independent replication.](figures/09_individual_sensitivity.png)

## 5 Discussion

### 5 1 Biological interpretation and alternative explanations

The zebra contrasts provide the clearest conditional evidence of differences among the available windows. Those differences are observations about a seasonal drought-to-rain sequence, not a controlled estimate of drought causation. The six animals are repeatedly observed, and only three selected calendar windows supply the phase labels. A period effect can represent temperature, forage, water availability, reproductive or social change, sampling, or several of these processes. A seasonal forest can reproduce some of that variation without having learned a drought-specific response.

Changes in the analyzed response are real changes in a derived measurement, subject to its recording limitations. Their biological meaning is more specific than the broad term behavior. A home-range area can change without a proportional change in distance traveled, and a daily distance can change without documenting feeding, drinking or stress. Likewise, proximity to a mapped water feature is not a measured visit or water intake. Conclusions stay at the level supported by the outcome.

Seasonal resource availability, temperature, reproductive or social state, location, management and observation effort are possible alternative explanations. The present records do not measure all of them sufficiently for comprehensive adjustment. Adding covariates indiscriminately is not a remedy: a covariate may be a mediator, be poorly scaled, or depend on the animal's movement itself. The selected models are transparent sensitivity analyses, not exhaustive causal models.

### 5 2 Association prediction and causation

The statistical and AI results should not be collapsed into a single statement that an animal changed because of drought. The regression concerns an adjusted association. Group-held-out prediction concerns transfer to unseen units. Forward validation concerns later observations with contemporaneous predictors. A five-stage causal comparison would require stronger control of calendar timing and shared exposure. Disaster anticipation would additionally require strictly pre-event predictors, event labels and a prospective warning target.

The source studies and this reanalysis also have different scopes. A smaller species-specific subset can lose exposure support that exists elsewhere in a multi-species study. A changed source version, index timescale or estimator can change a result. This manuscript does not claim to reproduce all original study findings, refute the original investigators, or demonstrate a new general law of animal disaster response.

### 5 3 Practical implications

The most informative extension would add the same calendar windows from independently characterized non-drought years and raw collar fix completeness. A second drought episode should be held entirely outside training. Late recovery should be defined from external environmental evidence and tested for behavioral equivalence using a prespecified meaningful tolerance.

### 5 4 Limitations and threats to validity

CD is already a drought period. HD and HW occur in different calendar months from CD, and the daily-distance table has no independent continuous drought covariate. Only six individuals support animal-clustered uncertainty. The source maximum and minimum temperature files are byte-identical, and hourly movement labels include issues, so those outcomes are not silently substituted into this analysis.

The analysis is exploratory and follows earlier inspection of these data. It is not preregistered. Stage thresholds, covariate sets and sensitivity decisions are documented, but the reported q-values do not incorporate every possible researcher decision. An apparently precise estimate can still be biased, and nominal clustering intervals are especially uncertain when the number of independent units or years is small.

Source tracking completeness cannot be reconstructed from the derived tables. No raw-fix error filter, location interpolation or missingness mechanism is independently validated here. Animals that survive or remain collared long enough to enter a complete sequence may differ from those that do not. A complete-case stage analysis can therefore select a nonrepresentative subset even when its date checks are correct.

Model settings were fixed to avoid test-driven tuning, but the validation design remains limited by the available records. Unit and time splits are separate rather than simultaneous unseen-animal-and-unseen-event tests. Exponentiating log predictions can produce scale-dependent ranking differences. No calibrated uncertainty model, threshold classifier, welfare prediction or real-time decision system is validated.

## 6 Conclusions and future research

Daily movement differs clearly between the observed periods under the specified model, but drought progression and season are inseparable. These results do not supply a genuine pre-drought baseline or a validated late-normal stage.

The contribution is a reproducible species-specific assessment of data support, adjusted association and predictive generalization. It does not convert absent baseline or recovery observations into evidence. Future studies should make independent drought episodes the design unit, specify environmental stage boundaries before looking at behavior, and retain untreated seasonal comparisons. Behavioral recovery should be tested using a prespecified equivalence margin rather than inferred from a nonsignificant difference or a later calendar date.

## 7 Data availability reproducibility and declarations

This manuscript is an AI-assisted secondary-analysis draft, not a peer-reviewed publication. It reports no new animal handling or field experiment. No authorship, institutional affiliation, ethics approval number, grant award, conflict-of-interest declaration or contribution history has been invented. The eventual submitting authors must provide and verify their own publication declarations and take responsibility for independent review.

The source investigators and repositories are credited below. Data and code are supplied with source hashes, original-version information, preprocessing rules, fitted statistical coefficients, model feature manifests, held-out predictions and split audits. The trained forest is an exploratory reproducibility artifact; its presence does not authorize a deployment claim. Original licences and attribution should accompany redistribution.

The retained primary analyses are documented in run_seven_species.py and elephant_five_stage_detail.py. The additional script three_paper_analysis.py refits the primary coefficients, runs every individual-deletion sensitivity, calculates paired period means and checks expanded calendar-stage identifiability. The authoring script builds these papers from retained result files; it does not choose models by statistical significance. Numerical results, model settings, predictions and source provenance are included. The preparation date is 22 November 2026.

## References

[1] Vera KB and colleagues. Data from Herbivore thermoregulation movement behavior and survival during a severe drought in Namibia. Dryad; 2026. https://doi.org/10.5061/dryad.9cnp5hr2g

[2] Vera KB and colleagues. Herbivore thermoregulation movement behaviour and survival during a severe drought in Namibia. Journal of Animal Ecology. Published online 2 November 2026. https://doi.org/10.1111/1365-2656.70387

[3] Breiman L. Random Forests. Machine Learning. 2001;45:5-32. https://doi.org/10.1023/A:1010933404324

[4] Roberts DR and colleagues. Cross-validation strategies for data with temporal spatial hierarchical or phylogenetic structure. Ecography. 2017. https://doi.org/10.1111/ecog.02881

[5] Benjamini Y, Hochberg Y. Controlling the False Discovery Rate A Practical and Powerful Approach to Multiple Testing. Journal of the Royal Statistical Society Series B. 1995;57:289-300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x

[6] scikit-learn documentation. GroupKFold and RandomForestRegressor. Accessed 22 November 2026. https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html ; https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html

[7] Qayyum B, Sarwar U, Saeed M, Qadeer A. Temporal Variation in Juvenile White Shark Diving Behavior Around Hurricane Blanca (2015): An Exploratory Case Study. User-supplied unpublished reference manuscript, Shark_Paper_Targeted_Revision.docx; publication date and journal not supplied. Used for structure and descriptive comparison, not as a source of terrestrial data.

## Appendix A Validation split audit

Group-held-out rows have disjoint unit membership by design. The dates in those splits can overlap because they assess new units rather than future periods. The following table reports forward splits only. Later test observations can share units with earlier training observations, but their dates respect the stated embargo. The complete split file also includes group-fold membership counts.

Table A1 Forward validation folds



| Fold | Training rows | Test rows | Last training date | First test date | Shared units |
| --- | --- | --- | --- | --- | --- |
| 0 | 93 | 180 | 2019-07-31 | 2019-11-01 | 3 |
| 1 | 273 | 123 | 2019-11-30 | 2020-02-01 | 5 |

## Appendix B Unit coverage

Coverage is presented to show unequal replication and temporal gaps. First and last dates do not imply continuous monitoring between them. For social species, a unit is the source social grouping used in the analysis, not necessarily one collared animal.

Table B1 Records and observed span by analytical unit



| Unit | Records | First date | Last date | Median response |
| --- | --- | --- | --- | --- |
| 3324EQ41 | 61 | 2019-07-01 | 2019-11-30 | 9.38 |
| 3326EQ33 | 85 | 2019-07-01 | 2020-02-24 | 12.54 |
| 3330EQ63 | 59 | 2019-11-01 | 2020-02-29 | 15.19 |
| 3331EQ62 | 59 | 2019-11-01 | 2020-02-29 | 10.19 |
| 3332EQ64 | 58 | 2019-11-01 | 2020-02-29 | 8.73 |
| EQ38 | 74 | 2019-07-01 | 2020-02-29 | 18.88 |

## Appendix C Evidence interpretation checklist

Table C1 What this manuscript does and does not establish



| Question | Assessment |
| --- | --- |
| Observed records analyzed | Yes with explicit source and preprocessing |
| Separate statistical model | Yes with conditional uncertainty and sensitivity |
| Separate AI model | Yes with saved settings and held-out evaluation |
| Complete five-stage support | 0 complete sequences under the stated rule |
| Normal behavior after drought | Not established by environmental normalization alone |
| Drought-specific causal effect | Not established by these observational models |
| Advance disaster prediction | Not tested or validated |
| Publication readiness | Requires independent scientific review and verified author declarations |
