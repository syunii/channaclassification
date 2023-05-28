import streamlit as st
from PIL import Image
from datetime import date

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico"
)

with st.container():    
    st.markdown(
        """
        <h1 style='text-align: center; color: #FFAC08;'>Channa Fish Classification Dashboard</h1>
        <p style='text-align: center;'>Welcome to the Fish Classification Dashboard!</p>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([10,10,10])

    with col1:
        st.write(' ')

    with col2:
        st.image("logo/android-chrome-512x512.png", width=250)

    with col3:
        st.write(' ')

with st.container():
    tab1, tab2 = st.tabs(["Tentang", "Panduan Pengguna"])

    with st.container():
        tab1.header(":orange[Tentang Ikan Channa]")
        tab1.write("Channa fish, also known as snakehead fish, are freshwater predatory fish found in Asia and Africa. They are known for their aggressive behavior and can survive in various habitats.")
        
        #channa andrao
        tab1.subheader(":orange[Ikan Channa Andrao]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/andrao.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Andrao\n
                Kingdom : Animalia\n
                Filum   : Chordata\n
                Famili  : Channidae\n
                Ordo    : Perciformes\n
                Kelas   : Actinopterygii\n
                Genus   : Channa\n
                Spesies : Channa andrao\n
                """
                )

        tab1.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
                   ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
                   ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara.""")
        
        #channa asiatica
        tab1.subheader(":orange[Ikan Channa Asiatica]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/asiatica.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Asiatica\n
                Kingdom : Animalia\n
                Filum   : Chordata\n
                Famili  : Channidae\n
                Ordo    : Perciformes\n
                Kelas   : Actinopterygii\n
                Genus   : Channa\n
                Spesies : Channa asiatica\n
                """
                )

        tab1.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
                   ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
                   ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara.""")

        #channa Auranti
        tab1.subheader(":orange[Ikan Channa Auranti]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/auranti.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Auranti\n
                Kingdom : Animalia\n
                Filum   : Chordata\n
                Famili  : Channidae\n
                Ordo    : Perciformes\n
                Kelas   : Actinopterygii\n
                Genus   : Channa\n
                Spesies : Channa aurantimaculata\n
                """
                )

        tab1.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
                   ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
                   ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara.""")    
    
        #channa barca
        tab1.subheader(":orange[Ikan Channa Barca]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/barca.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Barca\n
                Kingdom : Animalia\n
                Filum   : Chordata\n
                Famili  : Channidae\n
                Ordo    : Perciformes\n
                Kelas   : Actinopterygii\n
                Genus   : Channa\n
                Spesies : Channa barca\n
                """
                )

        tab1.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
                   ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
                   ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara.""")
    
        #channa maru
        tab1.subheader(":orange[Ikan Channa Maru]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/maru.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Maru\n
                Kingdom : Animalia\n
                Filum   : Chordata\n
                Famili  : Channidae\n
                Ordo    : Perciformes\n
                Kelas   : Actinopterygii\n
                Genus   : Channa\n
                Spesies : Channa marulius\n
                """
                )

        tab1.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
                   ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
                   ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara.""")
    
        #channa stewartii
        tab1.subheader(":orange[Ikan Channa Stewartii]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/stewartii.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Stewartii\n
                Kingdom : Animalia\n
                Filum   : Chordata\n
                Famili  : Channidae\n
                Ordo    : Perciformes\n
                Kelas   : Actinopterygii\n
                Genus   : Channa\n
                Spesies : Channa stewartii\n
                """
                )

        tab1.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
                   ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
                   ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara.""")
        
    with st.container():
        tab2.header(":orange[Cara Menggunakan Web Klasifikasi Gambar]")

        tab2.subheader(":orange[Langkah 1: Unggah Gambar]")
        tab2.write("1. Klik tombol 'Unggah Gambar' di halaman utama.")
        tab2.write("2. Pilih file gambar yang ingin Anda klasifikasikan dari perangkat Anda.")
        tab2.write("3. Tunggu hingga gambar selesai diunggah dan diproses.")

        tab2.subheader(":orange[Langkah 2: Tampilkan Hasil Klasifikasi]")
        tab2.write("1. Setelah gambar diproses, hasil klasifikasi akan ditampilkan di halaman Hasil.")
        tab2.write("2. Anda akan melihat label kategori atau kelas yang menggambarkan apa yang ada di gambar.")
        tab2.write("3. Jika tersedia, probabilitas atau skor klasifikasi untuk setiap kategori juga akan ditampilkan.")

        tab2.subheader(":orange[Langkah 3: Jelajahi Galeri Gambar]")
        tab2.write("1. Kunjungi halaman Galeri Gambar untuk melihat koleksi gambar yang telah diklasifikasikan sebelumnya.")
        tab2.write("2. Anda dapat menjelajahi gambar-gambar tersebut dan melihat label kategori yang terkait.")

        tab2.subheader(":orange[Catatan:]")
        tab2.write("- Pastikan gambar yang Anda unggah memiliki format yang didukung.")
        tab2.write("- Hasil klasifikasi mungkin tidak 100% akurat. Gunakanlah dengan kebijaksanaan.")

    #footer aplikasi
    footer_style = """
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117;
    color: #FAFAFA;
    text-align: center;
    padding: 10px;
    """

    st.markdown(
        """
        <footer style='{}'>
            © 2023, Synchronize Team
        </footer>
        """.format(footer_style),
        unsafe_allow_html=True
    )
