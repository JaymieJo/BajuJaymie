import streamlit as st

 # Data baju anak
baju_anak = [
    {"Nama": "Baju Anak Motif Hewan", "Harga": 100000, "Gambar": "WEBSITE/baju1"},
    {"Nama": "Baju Anak Motif Bunga", "Harga": 95000, "Gambar": "images/anak_flower.jpg"},
    {"Nama": "Baju Anak Motif Mobil", "Harga": 105000, "Gambar": "images/anak_car.jpg"},
    {"Nama": "Baju Anak Motif Buah", "Harga": 110000, "Gambar": "images/anak_fruit.jpg"}, 
    {"Nama": "Baju Anak Motif Kartun", "Harga": 120000, "Gambar": "images/anak_cartoon.jpg"},
    {"Nama": "Baju Anak Motif Polkadot", "Harga": 90000, "Gambar": "images/anak_polkadot.jpg"}, 
    {"Nama": "Baju Anak Motif Pelangi", "Harga": 115000, "Gambar": "images/anak_rainbow.jpg"},
    {"Nama": "Baju Anak Motif Bintang", "Harga": 100000, "Gambar": "images/anak_star.jpg"},
    {"Nama": "Baju Anak Motif Luar Angkasa", "Harga": 92000, "Gambar": "images/anak_space.jpg"},
]

# Judul aplikasi
st.title("Toko Baju Anak")

# Katalog baju anak
for baju in baju_anak:
    col1, col2 = st.columns([1, 3])

    with col1:
        # Tampilkan gambar
        st.image(baju["Gambar"], use_column_width=True)

    with col2:
        # Tampilkan nama dan harga baju
        st.subheader(baju["Nama"])
        st.write(f"*Harga:* Rp {baju['Harga']:,}")

# Keranjang belanja
keranjang = st.empty()

# Tombol tambah ke keranjang
def add_to_cart(baju):
    if baju in keranjang.empty():
        keranjang.empty()
    
    if baju not in keranjang:
        keranjang.write(f"* {baju['Nama']} - Rp {baju['Harga']:,}")

for baju in baju_anak:
    st.button(f"Tambah ke Keranjang ({baju['Nama']})", on_click=add_to_cart, args=(baju,))
