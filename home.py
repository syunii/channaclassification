import streamlit as st
from PIL import Image
from datetime import date

# Inisialisasi total kunjungan
if 'total_visits' not in st.session_state:
    st.session_state['total_visits'] = 0

# Menaikkan total kunjungan
st.session_state.total_visits += 1

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico",
)

with st.container():
    col1, col2 = st.columns([10,3])
    with col1:
        # Menampilkan tanggal
        current_date = date.today().strftime("%B %d, %Y")
        st.write("Today's date is:", current_date)
    with col2:
        # Menampilkan total kunjungan
        st.write("Total Kunjungan:", st.session_state.total_visits)

with st.container():    
    # Title and introduction
    st.markdown(
        """
        <h1 style='text-align: center;'>Channa Fish Classification Dashboard</h1>
        <p style='text-align: center;'>Welcome to the Fish Classification Dashboard!</p>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([10,10,10])

    with col1:
        st.write(' ')

    with col2:
        st.image("logo/android-chrome-512x512.png", caption='Channa Classification Logo', width=250)

    with col3:
        st.write(' ')

with st.container():
    tab1, tab2 = st.tabs(["Tentang", "Panduan Pengguna"])
    with st.container():
        tab1.subheader("Tentang")
        # Information about Channa fish
        tab1.subheader("About Channa Fish")
        tab1.write("Channa fish, also known as snakehead fish, are freshwater predatory fish found in Asia and Africa. They are known for their aggressive behavior and can survive in various habitats.")
    with st.container():
        tab2.header("Cara Menggunakan Web Klasifikasi Gambar")

        tab2.subheader("Langkah 1: Unggah Gambar")
        tab2.write("1. Klik tombol 'Unggah Gambar' di halaman utama.")
        tab2.write("2. Pilih file gambar yang ingin Anda klasifikasikan dari perangkat Anda.")
        tab2.write("3. Tunggu hingga gambar selesai diunggah dan diproses.")

        tab2.subheader("Langkah 2: Tampilkan Hasil Klasifikasi")
        tab2.write("1. Setelah gambar diproses, hasil klasifikasi akan ditampilkan di halaman Hasil.")
        tab2.write("2. Anda akan melihat label kategori atau kelas yang menggambarkan apa yang ada di gambar.")
        tab2.write("3. Jika tersedia, probabilitas atau skor klasifikasi untuk setiap kategori juga akan ditampilkan.")

        tab2.subheader("Langkah 3: Jelajahi Galeri Gambar")
        tab2.write("1. Kunjungi halaman Galeri Gambar untuk melihat koleksi gambar yang telah diklasifikasikan sebelumnya.")
        tab2.write("2. Anda dapat menjelajahi gambar-gambar tersebut dan melihat label kategori yang terkait.")

        tab2.subheader("Catatan:")
        tab2.write("- Pastikan gambar yang Anda unggah memiliki format yang didukung.")
        tab2.write("- Hasil klasifikasi mungkin tidak 100% akurat. Gunakanlah dengan kebijaksanaan.")


