import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Dashboard App ️‍🔥")

df = pd.read_csv("/workspaces/blank-app/data/4g-belts-dtot.csv")

##
### clean data
##

df['date'] = pd.to_datetime(df['Begin Time'])

#  Select Belt
selected_belt = st.selectbox(
    'Select Belt',
     df['Group'].unique())

# 'You selected belt: ', selected_belt

# Select Belt
df_updated = df[df['Group'] == selected_belt]

#  Select KPI
selected_KPI = st.selectbox(
    'Select KPI',
     df_updated.columns)

# 'You selected KPI: ', selected_KPI

##
### Plot data
##
df_plot = df_updated[['date', selected_KPI]]
st.write(f'{selected_KPI} vs {selected_belt}')
st.line_chart(df_plot.set_index("date"))



