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
    # Title and introduction
    st.markdown(
        """
        <h1 style='text-align: center;'>Channa Fish Classification Galeri</h1>
        <style>
        """,
        unsafe_allow_html=True
    )
    
    if len(image_files) == 0:
        st.warning("Tidak ada gambar dalam folder.")
    else:
        st.write(f"Jumlah gambar: {len(image_files)}")
        
        # Loop melalui setiap file gambar dalam folder
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image = open(image_path, "rb").read()
            prediction_path = os.path.splitext(image_path)[0] + ".txt"
            if os.path.exists(prediction_path):
                with open(prediction_path, "r") as f:
                    predicted_label = f.read()
            else:
                predicted_label = "Prediksi tidak tersedia"
            
            # Menampilkan gambar dan hasil prediksi
            col1, col2 = st.columns([10, 1])
            
            with col1:
                st.image(image, caption=image_file, use_column_width=True)
                st.info(f"Hasil prediksi: {predicted_label}")
            
            with col2:
                if st.button(f"❌", key=f"remove_{image_file}"):
                    os.remove(image_path)
                    # Mengupdate daftar file gambar setelah penghapusan
                    image_files.remove(image_file)
                    # Menghapus file hasil prediksi jika ada
                    if os.path.exists(prediction_path):
                        os.remove(prediction_path)

if __name__ == "__main__":
    main()
