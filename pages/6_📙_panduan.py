import streamlit as st

def main():
    st.title("Panduan Pengguna")

    st.header("Cara Menggunakan Web Klasifikasi Gambar")

    st.subheader("Langkah 1: Unggah Gambar")
    st.write("1. Klik tombol 'Unggah Gambar' di halaman utama.")
    st.write("2. Pilih file gambar yang ingin Anda klasifikasikan dari perangkat Anda.")
    st.write("3. Tunggu hingga gambar selesai diunggah dan diproses.")

    st.subheader("Langkah 2: Tampilkan Hasil Klasifikasi")
    st.write("1. Setelah gambar diproses, hasil klasifikasi akan ditampilkan di halaman Hasil.")
    st.write("2. Anda akan melihat label kategori atau kelas yang menggambarkan apa yang ada di gambar.")
    st.write("3. Jika tersedia, probabilitas atau skor klasifikasi untuk setiap kategori juga akan ditampilkan.")

    st.subheader("Langkah 3: Jelajahi Galeri Gambar")
    st.write("1. Kunjungi halaman Galeri Gambar untuk melihat koleksi gambar yang telah diklasifikasikan sebelumnya.")
    st.write("2. Anda dapat menjelajahi gambar-gambar tersebut dan melihat label kategori yang terkait.")

    st.subheader("Catatan:")
    st.write("- Pastikan gambar yang Anda unggah memiliki format yang didukung.")
    st.write("- Hasil klasifikasi mungkin tidak 100% akurat. Gunakanlah dengan kebijaksanaan.")

if __name__ == '__main__':
    main()
