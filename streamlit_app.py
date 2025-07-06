
import streamlit as st
import pandas as pd
from src.audit_tool import run_audit, generate_summary, load_data, load_config
from utils.penalty import estimate_penalty
from utils.roadmap import generate_roadmap

st.set_page_config(page_title="DPDP Compliance Dashboard", layout="wide")

st.title("🛡️ DPDP Compliance Dashboard for Fintechs")

uploaded_file = st.file_uploader("Upload Customer Data CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    config = load_config()
    audited_df = run_audit(df, config)
    summary = generate_summary(audited_df)
    penalty = estimate_penalty(summary["customers_with_violations"], summary["total_customers"])

    st.subheader("📋 Violation Summary")
    st.json(summary)

    st.subheader("💰 Penalty Projection")
    st.metric("Estimated Penalty (INR)", f"{penalty['estimated_penalty_inr']:,}")
    st.metric("Adjusted Penalty (INR)", f"{penalty['adjusted_penalty_inr']:,}")
    st.caption(f"Projected reduction: {penalty['penalty_reduction_pct']}%")

    st.subheader("📂 Download Audited Data")
    st.download_button("Download CSV", audited_df.to_csv(index=False).encode(), "audited_customers.csv", "text/csv")

    st.subheader("🧭 90-Day Roadmap")
    roadmap = pd.DataFrame(generate_roadmap())
    st.dataframe(roadmap)
    st.download_button("Download Roadmap", roadmap.to_csv(index=False).encode(), "90_day_roadmap.csv", "text/csv")
