import streamlit as st

# Buat judul halaman
st.title("Toko Baju Anak")

# Buat daftar produk
produk = [
    {"nama": "Baju Anak Laki-laki", "harga": 50000},
    {"nama": "Baju Anak Perempuan", "harga": 60000},
    {"nama": "Celana Anak Laki-laki", "harga": 45000},
    {"nama": "Rok Anak Perempuan", "harga": 55000},
]

# Tampilkan daftar produk
for produk in produk:
    st.write(f"{produk['nama']} - Rp{produk['harga']}")

# Buat sidebar untuk filter
st.sidebar.header("Filter")
kategori = st.sidebar.selectbox("Kategori", ("Semua", "Laki-laki", "Perempuan"))
harga_min = st.sidebar.number_input("Harga Minimum", min_value=0, max_value=1000000)
harga_max = st.sidebar.number_input("Harga Maksimum", min_value=0, max_value=1000000)

# Filter produk sesuai dengan pilihan pengguna
if kategori != "Semua":
    produk = [produk for produk in produk if produk["kategori"] == kategori]
if harga_min > 0:
    produk = [produk for produk in produk if produk["harga"] >= harga_min]
if harga_max > 0:
    produk = [produk for produk in produk if produk["harga"] <= harga_max]

# Buat keranjang belanja
st.session_state.keranjang = []

# Tambahkan tombol "Tambahkan ke Keranjang"
if st.button(f"Tambahkan ke Keranjang ({produk['nama']})"):
    st.session_state.keranjang.append(produk)

# Tampilkan ikon keranjang
st.sidebar.empty().button("Keranjang", key="keranjang")
