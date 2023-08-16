import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/cc.ico",
    layout="wide"
)

def main():
    st.title('Data 7 Jenis Ikan Channa yang Hidup di Air Tawar Bentopelagis Indonesia')
    st.write('Data Penjualan Per Bulan Agustus 2023')

    # URL atau path file CSV 
    url_or_path = 'data/channidae7.csv'  

    # Baca file CSV menjadi DataFrame
    try:
        df = pd.read_csv(url_or_path)
        # Tampilkan data sebagai tabel
        st.write('Sumber : fishbase.org')
        st.dataframe(df)
    except Exception as e:
        st.error(f"Tidak dapat membaca file CSV. Error: {e}")

def create_horizontal_bar_chart():
    # Data contoh (gantilah dengan data Anda sendiri dari sumber data)
    data = {
        'NamaIlmiah': ["Channa andrao", "Channa asiatica", "Channa aurantimaculata", "Channa barca", "Channa limbata", "Channa marulioides", "Channa stewartii"],
        'PenjualanTertinggi': [9200, 4800, 5400, 3000, 2000, 4300, 5200]
    }

    # Konversi data ke dalam DataFrame
    df = pd.DataFrame(data)

    # Urutkan DataFrame berdasarkan nilai PenjualanTertinggi secara menurun
    df.sort_values(by='PenjualanTertinggi', ascending=False, inplace=True)

    # Buat bar chart horizontal dengan warna berbeda pada setiap batang
    fig, ax = plt.subplots(figsize=(12, 6))
    y_pos = np.arange(len(df))
    colors = plt.cm.viridis(np.linspace(0, 1, len(df)))  # Pilih skema warna (ganti dengan yang lain jika diinginkan)
    bars = ax.barh(y_pos, df['PenjualanTertinggi'], color=colors, alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['NamaIlmiah'])
    ax.invert_yaxis()  # Agar produk terurut dari atas ke bawah
    ax.set_xlabel('Jumlah Penjualan')
    ax.set_title('Data Penjualan Tertinggi')

    # Tambahkan data labels di ujung setiap bar
    for bar, value in zip(bars, df['PenjualanTertinggi']):
        ax.text(value, bar.get_y() + bar.get_height()/2, str(value), ha='left', va='center', color='black', fontweight='bold')

    # Tampilkan chart di Streamlit
    st.pyplot(fig)

if __name__ == '__main__':
    main()
    create_horizontal_bar_chart()
