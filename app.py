import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sustainability Dashboard", layout="wide")
st.title("🌍 Sustainability Dashboard - Textile Company")

# Generate dummy sustainability data
dates = pd.date_range("2024-01-01", periods=30)
data = pd.DataFrame({
    "Date": dates,
    "Energy": np.random.randint(80, 150, 30),
    "Water": np.random.randint(200, 400, 30),
    "Waste": np.random.randint(10, 50, 30),
    "Emissions": np.random.randint(30, 70, 30),
})

# Sidebar filters
st.sidebar.header("🔎 Filters")
time_range = st.sidebar.selectbox("Time Range", ["Today", "Last 7 Days", "Last 30 Days", "Custom"])
unit = st.sidebar.selectbox("Unit", ["All Units", "Unit A", "Unit B"])
department = st.sidebar.selectbox("Department", ["All Departments", "Dyeing", "Weaving", "Finishing"])
shift = st.sidebar.selectbox("Shift", ["All Shifts", "Shift 1", "Shift 2", "Shift 3"])

# KPI Metrics
st.subheader("📊 KPI Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("⚡ Energy (kWh)", f"{data['Energy'].iloc[-1]}")
col2.metric("💧 Water (m³)", f"{data['Water'].iloc[-1]}")
col3.metric("🗑 Waste (kg)", f"{data['Waste'].iloc[-1]}")
col4.metric("🌫 Emissions (CO₂)", f"{data['Emissions'].iloc[-1]}")

# Overall Trend Chart
st.subheader("📈 Overall Performance Trends")
st.line_chart(data.set_index("Date"))

# Alerts Section
st.subheader("🚨 Critical Alerts")
alerts = data[data["Energy"] > 140]
if not alerts.empty:
    st.error(f"High Energy Usage Detected on {alerts['Date'].dt.date.tolist()}")
else:
    st.success("✅ All systems under control")

# Export Section
st.subheader("⬇ Export Data")
csv = data.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "sustainability_data.csv", "text/csv")

st.caption("Prototype Dashboard – expand with anomaly detection & goals tracking.")

