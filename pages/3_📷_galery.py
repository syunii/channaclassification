import streamlit as st

st.set_page_config(
    page_title="Channa Classification",
    page_icon="https://www.mediafire.com/file/1osnnszkwrjao0q/favicon.ico",
)

def main():
    st.title("Galeri Gambar")

    st.header("Gambar-gambar Terklasifikasi")

    # Daftar gambar yang telah diklasifikasikan sebelumnya
    image_list = [
        {
            'nama': 'Kucing',
            'gambar': 'https://example.com/path/to/cat.jpg'
        },
        {
            'nama': 'Anjing',
            'gambar': 'https://example.com/path/to/dog.jpg'
        },
        {
            'nama': 'Bunga',
            'gambar': 'https://example.com/path/to/flower.jpg'
        }
    ]

    # Tampilkan gambar-gambar dalam bentuk galeri
    for image in image_list:
        st.subheader(image['nama'])
        st.image(image['gambar'], caption=image['nama'], width=300)

if __name__ == '__main__':
    main()
