import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/cc.ico",
    layout="wide"
)

def main():
    st.title('Aplikasi Streamlit - Menampilkan Data dari CSV Tanpa Unggah File')

    # URL atau path file CSV (gantilah dengan URL atau path Anda)
    url_or_path = 'data\channidae_7.csv'  # Contoh URL
    # url_or_path = 'path/to/your/data.csv'      # Contoh path lokal

    # Baca file CSV menjadi DataFrame
    try:
        df = pd.read_csv(url_or_path)
        # Tampilkan data sebagai tabel
        st.write('Data dari file CSV:')
        st.dataframe(df)
    except Exception as e:
        st.error(f"Tidak dapat membaca file CSV. Error: {e}")

if __name__ == '__main__':
    main()
