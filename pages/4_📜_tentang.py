import streamlit as st

st.set_page_config(
    page_title="Channa Classification",
    page_icon="https://www.mediafire.com/file/1osnnszkwrjao0q/favicon.ico",
)

def main():
    st.title("Tentang Web Klasifikasi Gambar")

    st.header("Deskripsi")
    st.write("Web Klasifikasi Gambar adalah sebuah aplikasi yang menggunakan teknik klasifikasi gambar untuk mengenali objek atau kategori dalam sebuah gambar. Aplikasi ini didukung oleh model pembelajaran mesin yang telah dilatih menggunakan data gambar.")

    st.header("Tujuan")
    st.write("Tujuan dari proyek ini adalah untuk memberikan pengguna kemampuan untuk mengklasifikasikan gambar-gambar mereka dengan mudah dan cepat. Hal ini dapat bermanfaat dalam berbagai bidang seperti pengenalan pola, pengolahan citra, dan banyak lagi.")

    st.header("Teknologi")
    st.write("Web Klasifikasi Gambar dibangun menggunakan Python dan beberapa pustaka populer seperti TensorFlow, Keras, dan Streamlit. Model pembelajaran mesin yang digunakan untuk klasifikasi gambar dikembangkan dengan menggunakan teknik Deep Learning.")

    st.header("Tim")
    st.write("Proyek ini dikembangkan oleh Synchronize Team. Kami adalah tim yang terdiri dari pengembang dan peneliti di bidang kecerdasan buatan dan analisis data. Kami berkomitmen untuk menghadirkan solusi inovatif menggunakan teknologi terkini.")

    st.header("Kontak")
    st.write("Jika Anda memiliki pertanyaan atau masukan tentang proyek ini, jangan ragu untuk menghubungi kami di synchronize@gmail.com.")

if __name__ == '__main__':
    main()
