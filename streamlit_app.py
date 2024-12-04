import streamlit as st
import pandas as pd

# Load the data
baju_anak = pd.read_csv('data/baju_anak.csv')

# Create a sidebar for filtering the data
st.sidebar.header('Filter Baju Anak')
jenis_kelamin = st.sidebar.selectbox('Jenis Kelamin', ['Semua', 'Laki-laki', 'Perempuan'])
usia = st.sidebar.selectbox('Usia', ['Semua', '0-6 bulan', '6-12 bulan', '1-2 tahun', '2-3 tahun', '3-4 tahun'])
merek = st.sidebar.selectbox('Merek', ['Semua'] + baju_anak['Merek'].unique().tolist())
harga_min = st.sidebar.number_input('Harga Minimum', min_value=0, max_value=1000000)
harga_max = st.sidebar.number_input('Harga Maksimum', min_value=0, max_value=1000000)

# Filter the data
if jenis_kelamin != 'Semua':
    baju_anak = baju_anak[baju_anak['Jenis Kelamin'] == jenis_kelamin]
if usia != 'Semua':
    baju_anak = baju_anak[baju_anak['Usia'] == usia]
if merek != 'Semua':
    baju_anak = baju_anak[baju_anak['Merek'] == merek]
if harga_min > 0:
    baju_anak = baju_anak[baju_anak['Harga'] >= harga_min]
if harga_max < 1000000:
    baju_anak = baju_anak[baju_anak['Harga'] <= harga_max]

# Display the data
st.header('Katalog Baju Anak')
st.write(baju_anak)

# Create a scatter plot of the data
st.header('Scatter Plot of Baju Anak')
fig, ax = plt.subplots()
ax.scatter(baju_anak['Usia'], baju_anak['Harga'])
ax.set_xlabel('Usia')
ax.set_ylabel('Harga')
st.pyplot(fig)

# Create a bar chart of the data
st.header('Bar Chart of Baju Anak')
fig, ax = plt.subplots()
ax.bar(baju_anak['Merek'], baju_anak['Harga'])
ax.set_xlabel('Merek')
ax.set_ylabel('Harga')
st.pyplot(fig)

# Display the images of the baju anak
st.header('Gambar Baju Anak')
for i in range(len(baju_anak)):
    image = Image.open(f'images/{baju_anak["Gambar"][i]}')
    st.image(image, caption=baju_anak['Nama Produk'][i])
