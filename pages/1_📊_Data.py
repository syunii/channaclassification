import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/cc.ico",
    layout="wide"
)

def main():
    # Data yang akan ditampilkan (contoh data, Anda bisa sesuaikan dengan data sebenarnya)
    data = {
        "NamaIlmiah": ["Channa andrao", "Channa asiatica", "Channa aurantimaculata", "Channa barca", "Channa limbata", "Channa marulioides", "Channa stewartii"],
        "Penemu": ["Britz, 2013", "Linnaeus, 1758", "Musikasinthorn, 2000", "Hamilton, 1822", "Cuvier, 1831", "Bleeker, 1851", "Playfair, 1867"],
        "Penyebaran": ["India and Indonesia", "Indonesia, China, Taiwan, Viet Nam", "India and Indonesia", "India, Bangladesh and Indonesia", "Afghanistan in the west to Indonesia through South and Central Asia", "India to China, south to Thailand, Cambodia and Indonesia", "India, Indonesia and Nepal"],
        "MaxLength(cm)": [14.2, 20.0, 36.2, 105, 32.9, 27.0, 29.7],
        "PenjualanTertinggi": [9200, 4800, 5300, 2900, 1900, 4200, 8000]
    }

    # Membuat DataFrame dari data yang telah disiapkan
    df = pd.DataFrame(data)

    # Filter data sesuai kondisi dan kolom yang diminta
    df_min = df[df["PenjualanTertinggi"] > 1500][["NamaIlmiah", "Penemu", "Penyebaran", "MaxLength(cm)", "PenjualanTertinggi"]]

    # Urutkan berdasarkan nilai tertinggi pada kolom "PenjualanTertinggi"
    df_sorted = df_min.sort_values(by="PenjualanTertinggi", ascending=False)

    # Menampilkan judul aplikasi
    st.title('Hasil Filter dan Urutan Data')

    # Menampilkan data dalam bentuk tabel
    st.dataframe(df_sorted)

    # Menampilkan grafik menggunakan matplotlib
    plt.figure(figsize=(4, 3))
    plt.barh(df_sorted["NamaIlmiah"], df_sorted["PenjualanTertinggi"])
    plt.xticks(rotation=90)
    plt.xlabel("Nama Ilmiah")
    plt.ylabel("Penjualan Tertinggi")
    plt.title("Grafik Penjualan Tertinggi di Shopee")
    st.pyplot(plt)

if __name__ == '__main__':
    main()
