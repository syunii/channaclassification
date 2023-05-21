import streamlit as st
import os

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico",
)

# Path ke folder gambar
image_folder = "hasil"

# Mengambil daftar nama file gambar dalam folder
image_files = [f for f in os.listdir(image_folder) if f.endswith((".jpg", ".jpeg", ".png"))]

# Menampilkan halaman Streamlit
def main():
    st.title("Galeri Hasil Test")
    
    if len(image_files) == 0:
        st.warning("Tidak ada gambar dalam folder.")
    else:
        st.write(f"Jumlah gambar: {len(image_files)}")
        
        # Loop melalui setiap file gambar dalam folder
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image = open(image_path, "rb").read()
            
            # Menampilkan gambar dan tombol "Remove" di sebelah kanan
            col1, col2 = st.columns([10, 1])
            
            with col1:
                st.image(image, caption=image_file, use_column_width=True)
            
            with col2:
                if st.button(f"❌", key=f"remove_{image_file}"):
                    os.remove(image_path)
                    # Mengupdate daftar file gambar setelah penghapusan
                    image_files.remove(image_file)

if __name__ == "__main__":
    main()
