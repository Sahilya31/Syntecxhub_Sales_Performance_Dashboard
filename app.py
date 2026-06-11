import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

st.title("📊 Brand Sales Dashboard")

# -------------------------------
# KPI
total_sales = df['Sales'].sum()
st.metric("Total Sales", f"₹ {total_sales:,.0f}")

# -------------------------------
# Brand Filter
brand = st.selectbox("Select Brand", sorted(df['Brand'].unique()))
filtered_df = df[df['Brand'] == brand]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# -------------------------------
# 📈 Line Chart
st.subheader("📈 Sales Trend")
sales_trend = filtered_df.groupby('Order_Date')['Sales'].sum()
st.line_chart(sales_trend)

# -------------------------------
# 📊 Bar Chart
st.subheader("📊 Sales by Brand")
brand_sales = df.groupby('Brand')['Sales'].sum()
st.bar_chart(brand_sales)

# -------------------------------
# 🥧 Pie Chart (FIXED)
st.subheader("🥧 Market Share by Brand")

fig1, ax1 = plt.subplots()
ax1.pie(brand_sales, labels=brand_sales.index, autopct='%1.1f%%')
ax1.set_title("Brand Share")

st.pyplot(fig1)

# -------------------------------
# 📉 Histogram (NEW 🔥)
st.subheader("📉 Sales Distribution")

fig2, ax2 = plt.subplots()
ax2.hist(df['Sales'], bins=10)
ax2.set_title("Sales Distribution")

st.pyplot(fig2)
# Last updated: June 2026
