import streamlit as st
from PIL import Image
from datetime import date

    #tambah tentang web
    #tambah selengkapnya hyperlink
    #tentang team
st.set_page_config(
    page_title="Channa Classification - Check the Type of Channa",
    page_icon="logo/cc.ico"
)

with st.container():    
    st.markdown(
        """
        <h1 style='text-align: center; color: #289cd9;'>Klasifikasi 7 Jenis Channa Air Tawar Bentopelagis di Indonesia</h1>
        <p style='text-align: center;'>Check your channa, now!</p>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([10,10,10])

    with col1:
        st.write(' ')

    with col2:
        st.image("logo/cc.png", width=250)

    with col3:
        st.write(' ')


with st.container():
    tab1, tab2 , tab3= st.tabs(["Ikan Channa", "Panduan Pengguna", "Tentang Aplikasi"]) 

    with st.container():
        tab1.header(":blue[Sudah tahu ikan channa belum?]")
        tab1.write("""
                Ikan Channa adalah kelompok ikan air tawar yang terkenal dengan sebutan "snakehead fish" atau ikan kepala ular. Mereka memiliki penampilan yang khas dengan kepala mirip ular, badan memanjang, dan ekor bercabang. Ikan Channa memiliki kemampuan beradaptasi dengan berbagai kondisi perairan dan daya tahan yang tinggi. Beberapa spesies ikan Channa juga memiliki kemampuan untuk bergerak di darat. Keunikan dan daya tariknya membuat ikan Channa menjadi populer di kalangan penggemar ikan hias. Namun, beberapa spesies ikan Channa yang invasif dapat menyebabkan masalah ekologi di ekosistem asing. Oleh karena itu, pemeliharaan ikan Channa memerlukan perhatian khusus dan lingkungan yang sesuai.
        """
        )
    
    with st.container():
        tab1.subheader(":blue[Berikut 7 jenis ikan channa yang penyebarannya di Indonesia dan hidup di lingkungan air tawar bentopelagis, menurut data fishbase.org :]")

        #channa andrao
        tab1.subheader(":blue[1. Channa Andrao]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/andrao.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Andrao\n
                Kingdom : Animalia (hewan)\n
                Filum   : Chordata (vertebrata)\n
                Famili  : Channidae (ikan gabus)\n
                Ordo    : Perciformes (ikan bertulang belakang)\n
                Kelas   : Actinopterygii (ikan bersirip-jari)\n
                Genus   : Channa (gabus)\n
                Spesies : Channa andrao\n
                """
                )

        tab1.write("""Ikan Channa Andrao merupakan ikan yang berasa dari perairan Brahmaputra di timur laut India. Nama ikan Andrao berasal dari seorang penemu sekaligus ahli 
               ikan yang berasal dari India yaitu Andrew Rao, yang diresmikan pada tahun 2013 oleh dr. Ralf Britz. Ikan ini hidup di daerah beriklim tropis, sehingga ikan
               ini menjadi salah satu ikan channa favorit di Indonesia karena mudah untuk dipelihara. [Selengkapnya..](https://www.hobicupang.com/2022/12/ciri-ciri-ikan-channa-andrao.html)""")
        
        #channa asiatica
        tab1.subheader(":blue[2. Channa Asiatica]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/asiatica.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Asiatica\n
                Kingdom : Animalia (hewan)\n
                Filum   : Chordata (vertebrata)\n
                Famili  : Channidae (ikan gabus)\n
                Ordo    : Perciformes (ikan bertulang belakang)\n
                Kelas   : Actinopterygii (ikan bersirip-jari)\n
                Genus   : Channa (gabus)\n
                Spesies : Channa asiatica\n
                """
                )

        tab1.write("""Ikan Channa Asiatica merupakan salah satu jenis ikan gabus yang banyak dipelihara oleh penghobi ikan hias khususnya hobies ikan predator. 
                Nama lain dari ikan ini adalah small snakehead atau gabus kecil. Jenis ikan gabus ini merupakan salah satu dari empat jenis gabus lainnya yang 
                berasal dari negara China. Jenis gabus ini terdiri dari 2 jenis yang memiliki karakteristik berbeda, yaitu ikan channa asiatica white spot, dan 
                ikan channa asiatica red spot. [Selengkapnya..](https://www.ikanesia.id/2021/05/channa-asiatica.html)""")

        #channa Auranti
        tab1.subheader(":blue[3. Channa Auranti]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/auranti.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Auranti\n
                Kingdom : Animalia (hewan)\n
                Filum   : Chordata (vertebrata)\n
                Famili  : Channidae (ikan gabus)\n
                Ordo    : Perciformes (ikan bertulang belakang)\n
                Kelas   : Actinopterygii (ikan bersirip-jari)\n
                Genus   : Channa (gabus)\n
                Spesies : Channa aurantimaculata\n
                """
                )

        tab1.write("""Ikan Channa Auranti merupakan ikan yang bisa kita temui di Indonesia, karena memang sudah banyak yang membudidayakan. Namun, habitat asli 
                ikan Channa Auranti adalah berasal dari sungai Brahmaputera di India. Tepatnya di wilayah Dibrugargh, wilayah paling timur laut Assam, India yang 
                beriklim tropis. Di habitat aslinya, ikan ini dapat bertahan hidup di wilayah yang kelembapannya tinggi, dan suhu musim panas yang sangat panas.
                [Selengkapnya..](https://www.ikanesia.id/2021/08/mengenal-ikan-channa-auranti-jenis-ikan.html)""")
        
        #channa barca
        tab1.subheader(":blue[4. Channa Barca]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/barca.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Barca\n
                Kingdom : Animalia (hewan)\n
                Filum   : Chordata (vertebrata)\n
                Famili  : Channidae (ikan gabus)\n
                Ordo    : Perciformes (ikan bertulang belakang)\n
                Kelas   : Actinopterygii (ikan bersirip-jari)\n
                Genus   : Channa (gabus)\n
                Spesies : Channa barca\n
                """
                )

        tab1.write("""Channa barca merupakan ikan yang berasal dari India. Mereka merupakan hewan endemik di daerah sungai Brahmaputra dan Gangga, serta anak-anak 
                sungainya di bagian Assam. Selain di India, ikan eksotis ini juga menghuni sungai-sungai di daerah Bangladesh, terutama yang berdekatan dengan India.
                Channa barca memiliki tubuh yang memanjang, dengan bentuk silinder di bagian depan. Kemudian, bagian atas kepalanya ditutupi dengan sisik seperti piring. 
                Terdapat dua sisik bulat besar yang berada di kanan serta kiri rahang mulut bawahnya.   [Selengkapnya..](https://hewania.com/ikan-channa-barca/8751/)""")
    
        #channa limbata
        tab1.subheader(":blue[5. Channa Limbata]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/limbata.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Limbata\n
                Kingdom : Animalia (hewan)\n
                Filum   : Chordata (vertebrata)\n
                Famili  : Channidae (ikan gabus)\n
                Ordo    : Perciformes (ikan bertulang belakang)\n
                Kelas   : Actinopterygii (ikan bersirip-jari)\n
                Genus   : Channa (gabus)\n
                Spesies : Channa limbata\n
                """
                )

        tab1.write("""Channa limbata adalah ikan yang memiliki bentuk tubuh dengan kulit berwarna kecoklatan atau hitam
                   dengan bintik-bintik putih atau kuning pada bagian perut dan sisik-sisik yang besar. Ikan ini biasanya
                   hidup di air tawar seperti sungai, danau, atau rawa-rawa. Meskipun ukurannya relatif kecil, ikan ini
                   memiliki reputasi sebagai predator yang tangguh dan agresif, sehingga sering menjadi incaran bagi para pemancing.   [Selengkapnya..](https://www.hallocianjur.com/2023/02/channa-limbata-si-ikan-bogo-lokal-yang.html)""")
    

        #channa maru
        tab1.subheader(":blue[6. Channa Maru]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/maru.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Maru\n
                Kingdom : Animalia (hewan)\n
                Filum   : Chordata (vertebrata)\n
                Famili  : Channidae (ikan gabus)\n
                Ordo    : Perciformes (ikan bertulang belakang)\n
                Kelas   : Actinopterygii (ikan bersirip-jari)\n
                Genus   : Channa (gabus)\n
                Spesies : Channa marulius\n
                """
                )

        tab1.write("""Channa Maru merupakan salah satu jenis ikan yang populer dikalangan para pecinta ikan hias. Channa Maru mempunyai nama latin Channa Marulioides atau 
                Emperor Snakehead. Ikan ini merupakan ikan asli dari perairan Indonesia. Ikan ini menjadi populer karena harganya yang relatif murah, perawatan yang mudah, 
                dan tentunya karena warna corak yang indah. Channa maru ikan yang memiliki corak warna kuning paling terang di antara jenis channa. Ikan channa maru asal 
                Indonesia bahkan sudah menjadi primadona di seluruh dunia. [Selengkapnya..](https://www.alamikan.com/2022/05/channa-maru-ikan-gabus-hias-asli-dari.html)""")

        #channa stewartii
        tab1.subheader(":blue[7. Channa Stewartii]")
        with tab1.container():
            col1, col2 = st.columns([8, 9])
            with col1:
                st.image("assets/stewartii.png")
            with col2:
                st.write("""
                Klasifikasi Ikan Channa Stewartii\n
                Kingdom : Animalia (hewan)\n
                Filum   : Chordata (vertebrata)\n
                Famili  : Channidae (ikan gabus)\n
                Ordo    : Perciformes (ikan bertulang belakang)\n
                Kelas   : Actinopterygii (ikan bersirip-jari)\n
                Genus   : Channa (gabus)\n
                Spesies : Channa stewartii\n
                """
                )

        tab1.write("""Channa Stewartii merupakan spesies ikan gabus yang berasal dari Asia Selatan, lebih tepatnya di Negara India dan Nepal. Ikan ini juga dapat ditemukan 
                di negara Bangladesh. Habitat asli Channa Stewartii adalah sungai di pegunungan India. Ikan ini hidup di air dengan suhu sekitar 22 - 30 derajat Celcius dengan 
                kadar pH 5 - 7. Channa Stewartii memiliki corak dan warna yang mirip dengan Channa Barca, sehingga tak jarang kolektor ikan Channa menyebutnya Barca KW. [Selengkapnya..](https://www.alamikan.com/2022/05/channa-maru-ikan-gabus-hias-asli-dari.html)""")

    with st.container():
        tab2.header(":blue[Cara Menggunakan Aplikasi]")

        tab2.subheader(":blue[Melihat Data]")
        tab2.write("1. Kunjungi halaman 📊Data pada sidebar")
        tab2.write("2. Gulir ke bawah untuk melihat grafik data penjualan tertinggi")

        tab2.subheader(":blue[Mengklasifikasi Gambar Ikan]")
        tab2.write("1. Kunjungi halaman 🐟Klasifikasi pada sidebar")
        tab2.write("2. Klik tombol 'Unggah Gambar' di halaman Klasifikasi")
        tab2.write("3. Pilih file gambar yang ingin Anda klasifikasikan dari perangkat Anda")
        tab2.write("4. Tunggu hingga gambar selesai diunggah dan diproses, Anda akan melihat hasil klasifikasi dan juga rekomendasi toko beserta jumlah data penjualan di Shopee")
    
        tab2.subheader(":blue[Melihat Riwayat Klasifikasi]")
        tab2.write("1. Kunjungi halaman 🖼Galeri pada sidebar dan akan melihat semua riwayat hasil klasifikasi")
        tab2.write("2. Klik 'Pilih Jenis Channa' untuk melihat riwayat hasil klasifikasi jenis channa tertentu saja")
        tab2.write("3. Klik icon '🗑' untuk menghapus riwayat hasil klasifikasi")

        tab2.subheader(":blue[Menyampaikan Pertanyaan dan Saran]")
        tab2.write("1. Kunjungi halaman 📮Kontak pada sidebar")
        tab2.write("2. Isi formulir yang tersedia dengan sesuai dan lengkap")
        tab2.write("3. Klik tombol '📤Kirim Pesan'")

        tab2.subheader(":blue[Catatan:]")
        tab2.write("- Pastikan gambar yang Anda unggah memiliki format yang didukung dan berwarna.")
        tab2.write("- Hasil klasifikasi mungkin tidak 100% akurat. Gunakanlah dengan kebijaksanaan.")
    
    with st.container():
        tab3.header(":blue[Tentang Aplikasi]")
        tab3.write("""Channa Classification merupakan sebuah aplikasi berbasis website yang berfungsi untuk mengklasifikasikan sebuah gambar ikan channa ke dalam kelompok ikan channa tertentu.
            Saat ini, aplikasi mampu mendeteksi 7 jenis ikan channa yang penyebarannya termasuk di Indonesi serta hidup di lingkungan air tawar bentopelagis, yaitu Andrao, Asiatica, Auranti, Barca, Limbata, Maru dan Stewartii.
            Selain dapat mengklasifikasi, aplikasi juga mampu merekomendasikan toko penjual anakan ikan channa di Shopee yang terpercaya. Aplikasi masih dalam tahap pengembangan,
            yang tentunya memerlukan kritik dan saran dari pengguna.
        """)

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
            © 2023, Channa Classification
        </footer>
        """.format(footer_style),
        unsafe_allow_html=True
    )
