import streamlit as st
import pandas as pd
import plotly.express as px


st.header('Tossing a Coin')

# Read in Dataset
df_vehicles = pd.read_csv("vehicles_us.csv")

fig_price_dirst = px.histogram(df_vehicles['price'])

st.plotly_chart(fig_price_dirst)

fig_price_vs_condition = px.scatter(x=df_vehicles['condition'],y=df_vehicles['price'])

st.plotly_chart(fig_price_dirst)

st.header('Tossing a Coin')

st.write('It is not a functional application yet. Under construction.') 