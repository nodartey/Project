import streamlit as st
import pandas as pd
import plotly.express as px


st.header('Adverstisement of Cars')
st.write('Filter the data below to see the ads by manufacturer')


car_advertisement = pd.read_csv('vehicles_us.csv')
