import streamlit as st

# Buat tabel pelanggan jika belum ada
c.execute("""CREATE TABLE IF NOT EXISTS pelanggan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    nomor_telepon TEXT
)""")

# Buat tabel produk jika belum ada
c.execute("""CREATE TABLE IF NOT EXISTS produk (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    harga NUMERIC
)""")

# Fungsi untuk menambahkan pelanggan baru
def add_pelanggan(nama, nomor_telepon):
    c.execute("INSERT INTO pelanggan (nama, nomor_telepon) VALUES (?, ?)", (nama, nomor_telepon))
    conn.commit()

# Fungsi untuk mendapatkan daftar produk
def get_produk():
    c.execute("SELECT * FROM produk")
    return c.fetchall()

# Fungsi untuk menambahkan produk baru
def add_produk(nama, harga):
    c.execute("INSERT INTO produk (nama, harga) VALUES (?, ?)", (nama, harga))
    conn.commit()

# Judul Aplikasi
st.title("Kasir Toko Baju Bayi")

# Formulir Pembelian
with st.form("form_pembelian"):
    # Input Nama Pelanggan
    nama_pelanggan = st.text_input("Nama Pelanggan")

    # Input Nomor Telepon
    nomor_telepon = st.text_input("Nomor Telepon")

    # Input Daftar Produk yang Dibeli
    produk_dibeli = st.multiselect("Produk yang Dibeli", get_produk())

    # Input Jumlah Produk yang Dibeli
    jumlah_produk = st.number_input("Jumlah Produk", min_value=1)

    # Submit Button
    submit = st.form_submit_button("Proses Pembelian")
