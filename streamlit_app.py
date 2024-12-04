import streamlit as st
import pandas as pd

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
st.table(data)

# Buat tombol "Tambahkan ke Keranjang"
for i, row in data.iterrows():
    if st.button(f"Tambahkan ke Keranjang ({row['nama_produk']})"):
        st.session_state.keranjang.append(row.to_dict())

# Tampilkan ikon keranjang
st.sidebar.empty().button("Keranjang", key="keranjang")

# Tampilkan formulir pemesanan
st.form(key="form_pemesanan")
nama = st.text_input("Nama")
nomor_telepon = st.number_input("Nomor Telepon")
if st.form_submit_button("Pesan"):

    # Kirim informasi pesanan melalui email atau simpan ke database
import smtplib

# Alamat email pengirim
email_pengirim = "email_pengirim@domain.com"

# Alamat email penerima
email_penerima = "email_penerima@domain.com"

# Subjek email
subjek_email = "Pesanan dari Toko Baju Anak"

# Isi email
isi_email = f"""
Nama: {nama}
Nomor Telepon: {nomor_telepon}

Produk yang Dipesan:
"""

for produk in st.session_state.keranjang:
    isi_email += f"- {produk['nama_produk']} (Rp{produk['harga']})\n"

# Kirim email
smtplib.SMTP("smtp.domain.com", 587).sendmail(
    email_pengirim,
    email_penerima,
    f"Subject: {subjek_email}\n\n{isi_email}"
)
