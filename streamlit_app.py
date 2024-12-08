import streamlit as st
import pandas as pd
from streamlit_login_form import st_login_form

# Buat judul halaman
st.title("Toko Baju Anak")

# Buat sidebar untuk katalog produk
st.sidebar.header("Katalog Produk")
kategori = st.sidebar.selectbox("Kategori", ("Semua", "Laki-laki", "Perempuan"))
ukuran = st.sidebar.selectbox("Ukuran", ("Semua", "S", "M", "L"))
harga_min = st.sidebar.number_input("Harga Minimum", min_value=0, max_value=1000000)
harga_max = st.sidebar.number_input("Harga Maksimum", min_value=0, max_value=1000000)

# Muat data
data = pd.read_csv("data_baju_anak.csv")

# Filter data sesuai dengan pilihan pengguna
if kategori != "Semua":
    data = data[data["kategori"] == kategori]
if ukuran != "Semua":
    data = data[data["ukuran"] == ukuran]
if harga_min > 0:
    data = data[data["harga"] >= harga_min]
if harga_max > 0:
    data = data[data["harga"] <= harga_max]

# Buat sistem login
username = st.session_state.get("username", None)
if not username:
    username, password = st_login_form(submit_button_text="Login")
    if username and password:
        # Validasi kredensial login
        # ...

        # Simpan username ke sesi
        st.session_state.username = username

# Tampilkan produk
for i, row in data.iterrows():
    # Tampilkan gambar produk
    st.image(row["gambar_produk"], width=200)

# Tampilkan informasi produk
    st.write(f"{row['nama_produk']}")
    st.write(f"Rp{row['harga']}")

    # Tambahkan tombol "Tambahkan ke Keranjang"
    if st.button(f"Tambahkan ke Keranjang ({row['nama_produk']})"):
        # Tambahkan produk ke keranjang
        # ...

        # Tampilkan pemberitahuan waktu nyata
        st.success(f"{row['nama_produk']} telah ditambahkan ke keranjang.")

# Tampilkan opsi keranjang belanja
if username:
    # Dapatkan informasi keranjang pengguna
    # ...

    # Tampilkan ikon keranjang dan jumlah item
    st.write(f"Keranjang ({len(keranjang)} item)")

    # Tampilkan daftar item keranjang
    for item in keranjang:
        # Tampilkan gambar produk
        st.image(item["gambar_produk"], width=100)

        # Tampilkan informasi produk
        st.write(f"{item['nama_produk']}")
        st.write(f"Rp{item['harga']}")
        st.write(f"Jumlah: {item['jumlah']}")

        # Tambahkan tombol "Hapus dari Keranjang"
        if st.button(f"Hapus dari Keranjang ({item['nama_produk']})"):
            # Hapus item dari keranjang
            # ...

            # Tampilkan pemberitahuan waktu nyata
            st.success(f"{item['nama_produk']} telah dihapus dari keranjang.")

    # Tampilkan tombol "Checkout"
    if len(keranjang) > 0:
        if st.button("Checkout"):
            # Proses checkout
            # ...

            # Tampilkan konfirmasi checkout
            st.success("Checkout berhasil.")

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
