# DengAI — Reproducibility and Benchmark Provenance

This repository contains the project code/provenance for the manuscript **Climate-Coupled Variable-Order Fractional Dengue Dynamics with a Held-Out Gradient-Boosting Benchmark**.

## Public release status

The original competition data are **not redistributed**. DrivenData's official rules restrict participants from transmitting, publishing, redistributing, or otherwise making the competition Data available to non-participants. Public sharing of participant-developed source code is permitted subject to third-party rights.

The original 1,352 × 66 processed benchmark matrix and complete feature-generation pipeline were not recovered. Therefore this repository preserves the historical benchmark as **archived evidence**, not as an exactly rerunnable 61-feature dataset.

## Reproducibility release

See `reproducibility/` for:
- the verified 767/398/187 chronological split;
- the 13 history-feature names confirmed by the surviving Stage-5 code;
- the frozen Gradient Boosting configuration;
- archived benchmark metrics;
- archived Stage-6 diagnostics;
- the source-derived cohort reconstruction script;
- the reproducibility-status statement.

## DOI workflow

A GitHub release should be archived through Zenodo. Zenodo assigns the DOI to the release; the DOI must not be guessed or manually fabricated. After the DOI is assigned, it should be inserted into `CITATION.cff` and the manuscript Data Availability statement.

Official data source/rules:
https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/
