import streamlit as st
import pandas as pd
import os

# Buat judul halaman
st.title("Toko Baju Anak")

# Buat sidebar untuk katalog produk
st.sidebar.header("Katalog Produk")
kategori = st.sidebar.selectbox("Kategori", ("Semua", "Laki-laki", "Perempuan"))
ukuran = st.sidebar.selectbox("Ukuran", ("Semua", "S", "M", "L", "xl"))
harga_min = st.sidebar.number_input("Harga Minimum", min_value=0, max_value=1000000)
harga_max = st.sidebar.number_input("Harga Maksimum", min_value=0, max_value=1000000)

# Dapatkan jalur lengkap ke folder "baju_bayi"
folder_path = os.path.join(os.getcwd(), "baju_bayi")

# Muat daftar file gambar dalam folder
image_files = os.listdir(folder_path)

# Tampilkan daftar gambar produk
for image_file in image_files:
    # Dapatkan jalur lengkap ke setiap file gambar
    image_path = os.path.join(folder_path, image_file)

    # Tampilkan gambar produk
    st.image(image_path, width=200)
    
# Filter data sesuai dengan pilihan pengguna
if kategori != "Semua":
    data = data[data["kategori"] == kategori]
if ukuran != "Semua":
    data = data[data["ukuran"] == ukuran]
if harga_min > 0:
    data = data[data["harga"] >= harga_min]
if harga_max > 0:
    data = data[data["harga"] <= harga_max]


# Tampilkan produk
for i, row in data.iterrows():
    # Tampilkan gambar produk
    st.image(row["gambar_produk"], width=200)

# Tampilkan informasi produk
    st.write(f"{row['nama_produk']}")
    st.write(f"Rp{row['harga']}")



# Tampilkan help center
st.header("Help Center")

# Tampilkan FAQ
st.write("FAQ")
st.write("- Bagaimana cara memesan produk?")
st.write("- Bagaimana cara melacak pesanan saya?")
st.write("- Bagaimana cara mengembalikan produk?")

# Tampilkan dukungan pelanggan langsung
st.write("Dukungan Pelanggan Langsung")
st.write("Jika Anda memiliki pertanyaan atau butuh bantuan, silakan hubungi kami melalui email di support@toko-baju-anak.com atau telepon di 0812-3456-7890.")
