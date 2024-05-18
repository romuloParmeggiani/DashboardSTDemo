import streamlit as st
import pandas as pd
import plotly_express as px


st.set_page_config(layout="wide")


df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

month = st.sidebar.selectbox("Month", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Invoicing")
col1.plotly_chart(fig_date, use_container_width=True)

fig_product = px.bar(df_filtered, x="Date", y="Product line", color="City",
                     title="Product Invoicing", orientation="h")
col2.plotly_chart(fig_product, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Store Invoicing")
col3.plotly_chart(fig_city, use_container_width=True)

fig_paymethod = px.pie(df_filtered, values="Total", names="Payment", title="Payment Method")
col4.plotly_chart(fig_paymethod, use_container_width=True)

city_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_rating, x="Rating", y="City", title="Rating")
col5.plotly_chart(fig_rating, use_container_width=True)
