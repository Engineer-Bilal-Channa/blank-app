import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = pd.read_csv("/workspaces/blank-app/data/4g-belts-dtot.csv")

##
### clean data
##

df['date'] = pd.to_datetime(df['Begin Time'])
# Select Belt
df_s2 = df[df['Group'] == "South-2_LTE_2022"]


##
### Plot data
##
df_plot = df_s2[['date', 'OGS_LTE Availability_Inc_All Hours_Multi']]
st.line_chart(df_plot.set_index("date"))


# Select Belt
df_s2 = df[df['Group'] == "South-2_LTE_2022"]


##
### Plot data
##
df_plot = df_s2[['date', 'OGS_LTE Availability_Inc_All Hours_Multi']]
st.line_chart(df_plot.set_index("date"))

