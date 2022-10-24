import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

df = pd.read_csv('housing.csv')
plt.style.use('ggplot')
st.title('California Housing Data(1990)by ZigangZhu')

Median_house_pricing_filter = st.slider('Median_house_pricing_filter:', 0, 500001, 200000)
df = df[df.median_house_value >= Median_house_pricing_filter]

location_filter = st.sidebar.multiselect('Choose the location type',df.ocean_proximity.unique(), df.ocean_proximity.unique())
df = df[df.ocean_proximity.isin(location_filter)]

income_filter = st.sidebar.radio('Choose the income level',['Low','Medium','High'])
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
if income_filter == 'Medium':
    df = df[(df.median_income >= 2.5) & (df.median_income <= 4.5)]
if income_filter == 'High':
    df = df[df.median_income <= 4.5]        

st.subheader('See more filters in the sidebar:')
st.map(df)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(15, 10))
val = df.median_house_value.hist(bins=30)
st.pyplot(fig)