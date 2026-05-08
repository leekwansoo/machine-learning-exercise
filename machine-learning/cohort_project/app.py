import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cohort Dashboard", layout="wide")

FILE = "input/어린이코호트 임상데이터.xlsx"
df = pd.read_excel(FILE, sheet_name=0, engine="openpyxl")

st.title("Cohort Dashboard (여아 6-10)")

# Filters
ages = sorted(df["나이"].unique())
age_sel = st.multiselect("Select ages", ages, default=ages)
fdf = df[df["나이"].isin(age_sel)].copy()

st.write(f"Rows: {len(fdf)}")

# Numeric summary
num = fdf.select_dtypes(include="number")
st.subheader("Summary (describe)")
st.dataframe(num.describe())

# Correlation
st.subheader("Correlation")
st.dataframe(num.corr())

# Outliers (simple IQR)
st.subheader("Outlier Counts (IQR)")
out = []
for col in num.columns:
    q1, q3 = num[col].quantile(0.25), num[col].quantile(0.75)
    iqr = q3 - q1
    lo, hi = q1 - 1.5*iqr, q3 + 1.5*iqr
    out.append([col, int(((num[col] < lo) | (num[col] > hi)).sum())])
st.dataframe(pd.DataFrame(out, columns=["Column","Outlier_Count"]).sort_values("Outlier_Count", ascending=False))

# Quick plots
st.subheader("Distributions")
col = st.selectbox("Pick a column", num.columns.tolist())
st.bar_chart(num[col].value_counts().sort_index())