import streamlit as st
import pandas as pd
import plotly.express as px


st.header('Data Trends in Vehicle Data')

# Read in Dataset
df_vehicles = pd.read_csv("vehicles_us.csv")

fig_price_dirst = px.histogram(df_vehicles['price'])


st.write('The Price dirstribution of the vheicles is very right skwed.') 

st.plotly_chart(fig_price_dirst)

st.write('The most intresting trend is with the condition of the vehicles,  it seems that "good" contion is all that is required to get a good sale price for the veichles.') 

fig_price_vs_condition = px.scatter(x=df_vehicles['condition'],y=df_vehicles['price'])

st.plotly_chart(fig_price_vs_condition)
