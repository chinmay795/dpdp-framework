
# DPDP Compliance Framework for Indian Fintechs 🇮🇳

A self-contained toolset to help Indian fintech startups comply with the **Digital Personal Data Protection (DPDP) Act 2023**.  
Includes a Python audit engine, a Streamlit dashboard, synthetic data, and a 90-day compliance roadmap.

---

## 📦 Features

- ✅ Automated audit of customer records against 3 core DPDP rules
- 📊 Compliance dashboard with Streamlit
- 📉 Penalty estimation module (INR and % reduction)
- 🧭 90-Day compliance roadmap generator
- 🔐 Configurable thresholds for risk tuning

---

## 🛠️ Project Structure

```
├── data/               → Synthetic + audited customer datasets  
├── src/                → Python audit tool  
├── utils/              → Penalty and roadmap logic  
├── dashboard/          → Streamlit frontend  
├── reports/            → Exported roadmap reports  
├── config.json         → Thresholds (e.g., breach reporting delay)  
├── README.md
```

---

## 🚀 How to Use

### 1. Install dependencies  
```bash
pip install streamlit pandas
```

### 2. Run Streamlit dashboard  
```bash
streamlit run dashboard/streamlit_app.py
```

### 3. Run standalone audit  
```bash
python src/audit_tool.py
```

### 4. Export roadmap  
```bash
python reports/generate_roadmap_report.py
```

---

## 📌 Example: DPDP Rules Implemented
- ✅ Consent not given  
- 🌐 Unsafe cross-border data sharing  
- ⚠️ Breach reported after threshold (e.g., 3 days)

---

## 📈 Penalty Simulation  
Estimate total and adjusted penalties based on compliance efforts (e.g., INR 4.7 Cr → INR 2.9 Cr with 38% mitigation).

---

## 🧪 Based On
- DPDP Act 2023  
- GDPR Mapping  
- Inputs from 27 fintech professionals

---

## 🧑‍💻 Author  
This is part of a self-initiated compliance project to prepare startups for regulatory readiness in India.

