
import pandas as pd
import json
import os
from utils.penalty import estimate_penalty

def load_data(path):
    return pd.read_csv(path)

def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)

def run_audit(df, config):
    df["violation_consent_missing"] = ~df["consent_given"]
    df["violation_crossborder_unsafe"] = df["data_shared_crossborder"] & ~df["has_safeguards"]
    df["violation_breach_late"] = df["data_breach_reported"] & (df["breach_report_days"] > config["breach_report_threshold_days"])

    df["total_violations"] = df[[
        "violation_consent_missing",
        "violation_crossborder_unsafe",
        "violation_breach_late"
    ]].sum(axis=1)

    return df

def save_audited_data(df, output_path="data/audited_customers.csv"):
    df.to_csv(output_path, index=False)

def generate_summary(df):
    summary = {
        "total_customers": len(df),
        "customers_with_violations": int((df["total_violations"] > 0).sum()),
        "violation_counts": {
            "consent_missing": int(df["violation_consent_missing"].sum()),
            "crossborder_unsafe": int(df["violation_crossborder_unsafe"].sum()),
            "breach_late": int(df["violation_breach_late"].sum())
        }
    }
    return summary

if __name__ == "__main__":
    config = load_config()
    df = load_data("data/synthetic_customers.csv")
    audited_df = run_audit(df, config)
    save_audited_data(audited_df)
    summary = generate_summary(audited_df)
    penalty_info = estimate_penalty(summary["customers_with_violations"], total=len(df))
    print(json.dumps({**summary, **penalty_info}, indent=2))
