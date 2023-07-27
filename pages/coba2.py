import streamlit as st
import pandas as pd

# Contoh data
data = {
    'Kategori': ['Kategori A', 'Kategori B', 'Kategori C'],
    'Penjualan': [100, 200, 150]
}

df = pd.DataFrame(data)

# Membuat bar chart menggunakan st.bar_chart()
st.bar_chart(df['Penjualan'])

# Menambahkan data label ke dalam bar chart
for i, penjualan in enumerate(df['Penjualan']):
    st.text(f"{df['Kategori'][i]}: {penjualan}")
