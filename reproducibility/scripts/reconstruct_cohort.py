from pathlib import Path
import pandas as pd

FEATURES = Path("dengue_features_train.csv")
LABELS = Path("dengue_labels_train.csv")
OUT = Path("reconstructed_cohort_1352.csv")
KEYS = ["city", "year", "weekofyear"]

def main() -> None:
    features = pd.read_csv(FEATURES)
    labels = pd.read_csv(LABELS)
    df = features.merge(labels, on=KEYS, how="inner", validate="one_to_one")
    df["week_start_date"] = pd.to_datetime(df["week_start_date"])
    df = df.sort_values(["city", "week_start_date"]).reset_index(drop=True)
    df["cases_lag_52"] = df.groupby("city")["total_cases"].shift(52)
    cohort = (
        df.loc[df["cases_lag_52"].notna()]
        .sort_values("week_start_date")
        .reset_index(drop=True)
    )
    source_cols = list(features.columns) + ["total_cases"]
    cohort[source_cols].to_csv(OUT, index=False)

    assert len(cohort) == 1352
    checks = {
        766: "2003-10-08",
        767: "2003-10-15",
        1164: "2007-08-06",
        1165: "2007-08-13",
        1351: "2010-06-25",
    }
    for idx, expected in checks.items():
        actual = str(cohort.iloc[idx].week_start_date.date())
        assert actual == expected, (idx, actual, expected)

    print(f"Verified cohort: {cohort.shape[0]} rows x {cohort.shape[1]} columns")
    print("Verified chronological split: 767 train / 398 validation / 187 test")

if __name__ == "__main__":
    main()
