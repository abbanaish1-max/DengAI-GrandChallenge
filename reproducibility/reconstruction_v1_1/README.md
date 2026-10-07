# Source reconstruction v1.1.0

This release documents a deterministic reconstruction of the DengAI benchmark from the authoritative training feature and label files.

The reconstruction produces exactly 1,352 retained observations and 66 analysis columns: 4 identifier/time fields, 61 predictors, and total_cases.

Feature construction:
- 13 confirmed history features from the surviving Stage-5 feature-group code.
- 20 contemporaneous climate predictors.
- Seven lagged climate base variables selected using absolute Spearman correlation with total_cases on the training cohort only.
- Climate lags: 1, 2, 4, and 8 weeks.
- Missing climate values: city-specific medians fitted on the training cohort only, with a global training median fallback.
- History rolling statistics use shift(1) followed by rolling windows of 4, 8, and 12 weeks.

The model is frozen as GradientBoostingRegressor with 300 trees, learning rate 0.03, depth 3, min split 5, min leaf 2, and random_state 42.

Evaluation is chronological: 767 train / 398 validation / 187 test.

This is a source reconstruction, not a claim that the reconstructed CSV is byte-identical to a historical processed artifact.

The public release does not contain the DengAI competition source data or row-level derived files. Authorized users should place the original training feature and label files beside the reconstruction script before running it.