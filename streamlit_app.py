import streamlit as st
import pandas as pd
import numpy as np
import time


st.title("Dashboard App ️‍🔥")

# sidebar
with st.sidebar:
    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    with st.sidebar:
        selected_tech = st.selectbox(
            'Select Technology',
            ['4G', '3G', '2G']
        )

    # Clea Data
    df['date'] = pd.to_datetime(df['Begin Time'])

    with st.sidebar:
        #  Select Belt
        selected_belt = st.selectbox(
            'Select Belt',
            df['Group'].unique())

    # Selected Belt
    df_updated = df[df['Group'] == selected_belt]

    with st.sidebar:
        #  Select KPI
        selected_KPI = st.selectbox(
            'Select KPI',
            df_updated.columns)

    # Plot data
    df_plot = df_updated[['date', selected_KPI]]
    st.write(f'{selected_KPI} vs {selected_belt}')
    st.line_chart(df_plot.set_index("date"))

else:
    st.write("No file Uploaded!")
    st.write("Please upload a file to see dashboard view")