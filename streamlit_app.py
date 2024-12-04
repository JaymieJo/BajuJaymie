import streamlit as st
import pandas as pd

# Load the data
baju_anak = pd.read_csv('data/baju_anak.csv')

# Create a search bar
search_term = st.text_input('Cari Baju Anak')

# Filter the data
if search_term:
    baju_anak = baju_anak[baju_anak['Nama'].str.contains(search_term)]

# Display the data
st.header('Katalog Baju Anak')
st.write(baju_anak)
