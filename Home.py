import streamlit as st
from PIL import Image
from datetime import date

    #tambah tentang web
    #tambah selengkapnya hyperlink
    #tentang team
st.set_page_config(
    page_title="Channa Fish Classification",
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
    tab1, tab2 , tab3= st.tabs(["Tentang Aplikasi", "Panduan Pengguna", "Tentang Channa"])

    with st.container():
        tab1.header(":orange[Tentang Aplikasi]")
        tab1.write("""Channa Fish Classification merupakan sebuah aplikasi berbasis website yang berfungsi untuk mengklasifikasikan sebuah gambar ikan channa ke dalam kelompok ikan channa tertentu.
            Saat ini, aplikasi mampu mendeteksi 6 jenis ikan Channa yang terpopuler di Indonesia seperti Asiatica, Auranti, Andrao, Barca, Maru dan Stewartii. Aplikasi masih dalam tahap pengembangan
            tentunya memerlukan kritik dan saran dari pengguna.
        """)
    
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

    with st.container():
        tab3.header(":orange[Tentang Ikan Channa]")
        tab3.write("""
                Ikan Channa adalah ikan air tawar predator yang berasal dari Asia. Mereka memiliki penampilan menarik dengan tubuh ramping, warna yang beragam, dan ukuran yang bisa mencapai satu meter. 
                Ikan Channa agresif dan kuat, memakan serangga, krustasea, dan ikan kecil. Mereka populer di kalangan penghobi akuarium, tetapi juga dianggap sebagai spesies invasif di beberapa wilayah. 
                Oleh karena itu, penting untuk memelihara dan mengatur kepemilikan ikan Channa sesuai dengan peraturan setempat.
        """
        )
        
        #channa andrao
        tab3.subheader(":orange[Ikan Channa Andrao]")
        with tab3.container():
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

        tab3.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
               ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
               ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara. [selengkapnya..](https://www.hobicupang.com/2022/12/ciri-ciri-ikan-channa-andrao.html)""")
        
        #channa asiatica
        tab3.subheader(":orange[Ikan Channa Asiatica]")
        with tab3.container():
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

        tab3.write("""Ikan Channa Asiatica merupakan salah satu jenis ikan gabus yang banyak dipelihara oleh penghobi ikan hias khususnya hobies ikan predator. 
                Nama lain dari ikan ini adalah small snakehead atau gabus kecil. Jenis ikan gabus ini merupakan salah satu dari empat jenis gabus lainnya yang 
                berasal dari negara China. Jenis gabus ini terdiri dari 2 jenis yang memiliki karakteristik berbeda, yaitu ikan channa asiatica white spot, dan 
                ikan channa asiatica red spot. [selengkapnya..](https://www.ikanesia.id/2021/05/channa-asiatica.html)""")

        #channa Auranti
        tab3.subheader(":orange[Ikan Channa Auranti]")
        with tab3.container():
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

        tab3.write("""Ikan Channa Auranti merupakan ikan yang bisa kita temui di Indonesia, karena memang sudah banyak yang membudidayakan. Namun, habitat asli 
                ikan Channa Auranti adalah berasal dari sungai Brahmaputera di India. Tepatnya di wilayah Dibrugargh, wilayah paling timur laut Assam, India yang 
                beriklim tropis. Di habitat aslinya, ikan ini dapat bertahan hidup di wilayah yang kelembapannya tinggi, dan suhu musim panas yang sangat panas.
                [selengkapnya..](https://www.ikanesia.id/2021/08/mengenal-ikan-channa-auranti-jenis-ikan.html)""")
        
        #channa barca
        tab3.subheader(":orange[Ikan Channa Barca]")
        with tab3.container():
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

        tab3.write("""Channa barca merupakan ikan yang berasal dari India. Mereka merupakan hewan endemik di daerah sungai Brahmaputra dan Gangga, serta anak-anak 
                sungainya di bagian Assam. Selain di India, ikan eksotis ini juga menghuni sungai-sungai di daerah Bangladesh, terutama yang berdekatan dengan India.
                Channa barca memiliki tubuh yang memanjang, dengan bentuk silinder di bagian depan. Kemudian, bagian atas kepalanya ditutupi dengan sisik seperti piring. 
                Terdapat dua sisik bulat besar yang berada di kanan serta kiri rahang mulut bawahnya.   [selengkapnya..](https://hewania.com/ikan-channa-barca/8751/)""")
    
        #channa maru
        tab3.subheader(":orange[Ikan Channa Maru]")
        with tab3.container():
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

        tab3.write("""Channa Maru merupakan salah satu jenis ikan yang populer dikalangan para pecinta ikan hias. Channa Maru mempunyai nama latin Channa Marulioides atau 
                Emperor Snakehead. Ikan ini merupakan ikan asli dari perairan Indonesia. Ikan ini menjadi populer karena harganya yang relatif murah, perawatan yang mudah, 
                dan tentunya karena warna corak yang indah. Channa maru ikan yang memiliki corak warna kuning paling terang di antara jenis channa. Ikan channa maru asal 
                Indonesia bahkan sudah menjadi primadona di seluruh dunia. [selengkapnya..](https://www.alamikan.com/2022/05/channa-maru-ikan-gabus-hias-asli-dari.html)""")
    
        #channa stewartii
        tab3.subheader(":orange[Ikan Channa Stewartii]")
        with tab3.container():
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

        tab3.write("""Channa Stewartii merupakan spesies ikan gabus yang berasal dari Asia Selatan, lebih tepatnya di Negara India dan Nepal. Ikan ini juga dapat ditemukan 
                di negara Bangladesh. Habitat asli Channa Stewartii adalah sungai di pegunungan India. Ikan ini hidup di air dengan suhu sekitar 22 - 30 derajat Celcius dengan 
                kadar pH 5 - 7. Channa Stewartii memiliki corak dan warna yang mirip dengan Channa Barca, sehingga tak jarang kolektor ikan Channa menyebutnya Barca KW. [selengkapnya..](https://www.alamikan.com/2022/05/channa-maru-ikan-gabus-hias-asli-dari.html)""")
        
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
