import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Buat judul halaman
st.title("Toko Baju Anak")

# Buat sidebar untuk filter
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

# Buat keranjang belanja
st.session_state.keranjang = []

# Tampilkan data
st.header("Daftar Produk")
for i, row in data.iterrows():
    # Buat tombol "Tambahkan ke Keranjang"
    if st.button(f"Tambahkan ke Keranjang ({row['nama_produk']})"):
        st.session_state.keranjang.append(row.to_dict())
    
    # Tampilkan informasi produk
    st.write(f"{row['nama_produk']} - Rp{row['harga']}")

# Tampilkan ikon keranjang
st.sidebar.empty().button("Keranjang", key="keranjang")

# Tampilkan formulir pemesanan
st.form(key="form_pemesanan")
nama = st.text_input("Nama")
alamat = st.text_input("Alamat")
nomor_telepon = st.number_input("Nomor Telepon")
if st.form_submit_button("Pesan"):
    # Kirim informasi pesanan melalui email atau simpan ke database

# Tampilkan visualisasi data
st.header("Visualisasi Data")
fig = px.bar(data, x="kategori", y="harga")
st.plotly_chart(fig)
