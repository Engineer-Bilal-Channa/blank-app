import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Dashboard App ️‍🔥")

# df = pd.read_csv("/workspaces/blank-app/data/4g-belts-dtot.csv")

# upload file

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Show the first 5 rows of the CSV
    st.write("Preview of the CSV file:")
    st.dataframe(df)

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
