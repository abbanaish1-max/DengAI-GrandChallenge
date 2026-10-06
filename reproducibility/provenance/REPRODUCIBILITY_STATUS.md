# Reproducibility status

**Release status: archived benchmark + source-derived reconstruction.**

## Confirmed
- 1,352 retained cohort rows.
- Historical benchmark description: 66 columns / 61 predictors / target `total_cases`.
- 767/398/187 chronological split.
- 13 named history features.
- Environmental group defined as the remaining X_train columns (48 predictors).
- Frozen Gradient Boosting configuration.
- Archived full/history-only/environment-only metrics.
- Archived Stage-6 diagnostics.

## Not recovered
- Original 1,352 × 66 processed CSV.
- Exact 48 environmental feature names/order.
- Exact rolling construction and climate missing-value processing.
- Original benchmark notebook/script.
- Original software environment and serialized model.

## Interpretation
This is a transparent provenance/reproduction release. It must not be described as an exact regeneration of the historical 61-feature benchmark unless the missing artifacts are subsequently recovered and independently reconciled.
