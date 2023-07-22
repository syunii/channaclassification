import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_horizontal_bar_chart():
    # Data contoh (gantilah dengan data Anda sendiri dari sumber data)
    data = {
        'NamaIlmiah': ["Channa andrao", "Channa asiatica", "Channa aurantimaculata", "Channa barca", "Channa limbata", "Channa marulioides", "Channa stewartii"],
        'PenjualanTertinggi': [9200, 4800, 5300, 2900, 1900, 4200, 8000]
    }

    # Konversi data ke dalam DataFrame
    df = pd.DataFrame(data)

    # Urutkan DataFrame berdasarkan nilai PenjualanTertinggi secara menurun
    df.sort_values(by='PenjualanTertinggi', ascending=False, inplace=True)

    # Buat bar chart horizontal
    fig, ax = plt.subplots(figsize=(10, 6))
    y_pos = np.arange(len(df))
    ax.barh(y_pos, df['PenjualanTertinggi'], align='center', color='skyblue', alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['NamaIlmiah'])
    ax.invert_yaxis()  # Agar produk terurut dari atas ke bawah
    ax.set_xlabel('Penjualan Tertinggi')
    ax.set_title('Bar Chart Horizontal - Penjualan Tertinggi')

    # Tampilkan chart di Streamlit
    st.pyplot(fig)

def main():
    st.title('Contoh Bar Chart Horizontal dengan Penjualan Tertinggi di Streamlit')
    create_horizontal_bar_chart()

if __name__ == '__main__':
    main()
