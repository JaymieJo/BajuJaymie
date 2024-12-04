import streamlit as st
import pandas as pd
import numpy as np

# Buat judul halaman
st.title("Toko Baju Anak")

# Buat sidebar untuk memilih kategori dan kisaran harga
st.sidebar.header("Filter")
kategori = st.sidebar.selectbox("Kategori", ("Semua", "Laki-laki", "Perempuan"))
harga_min = st.sidebar.number_input("Harga Minimum", min_value=0, max_value=1000000)
harga_max = st.sidebar.number_input("Harga Maksimum", min_value=0, max_value=1000000)

# Muat data
data = pd.read_csv("data_baju_anak.csv")

# Filter data sesuai dengan pilihan pengguna
if kategori != "Semua":
    data = data[data["kategori"] == kategori]
if harga_min > 0:
    data = data[data["harga"] >= harga_min]
if harga_max > 0:
    data = data[data["harga"] <= harga_max]

# Tampilkan data
st.header("Daftar Produk")
st.table(data)
