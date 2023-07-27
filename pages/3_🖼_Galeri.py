import streamlit as st
import os
from PIL import Image
import glob
import datetime

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/cc.ico"
)

# Path to the image folder
image_folder = "hasil"

# Get the list of image file names in the folder sorted by creation time
image_files = sorted(
    [f for f in glob.glob(os.path.join(image_folder, "*.jpg"))],
    key=lambda f: os.path.getmtime(f),
    reverse=True,
)

# Display the Streamlit page
def main():
    st.title(":blue[Galeri Hasil Klasifikasi]")
    
    if len(image_files) == 0:
        st.warning("Tidak ada gambar dalam folder.")
    else:
        st.write(f"Jumlah total riwayat : {len(image_files)}")
        
        # Filter options
        fish_options = ["Semua","Andrao", "Asiatica", "Auranti", "Barca", "Limbata", "Stewartii", "Bukan Channa",  ]
        selected_fish = st.selectbox("Pilih Jenis Channa 🔽", fish_options)
        
        # Calculate the target size for cropping
        target_width = 600
        target_height = 300
        
        # Loop through each image file in the folder
        for i, image_file in enumerate(image_files):
            image = Image.open(image_file)
            
            # Get the predicted label
            prediction_file = os.path.splitext(image_file)[0] + ".txt"
            if os.path.exists(prediction_file):
                with open(prediction_file, "r") as f:
                    predicted_label = f.read()
            else:
                predicted_label = "Prediksi tidak tersedia"
            
            # Get the prediction date
            prediction_date = datetime.datetime.fromtimestamp(os.path.getmtime(prediction_file))
            
            # Filter images based on selected fish
            if selected_fish.lower() != "semua" and selected_fish.lower() not in predicted_label.lower():
                continue
            
            # Crop the image to have the target dimensions
            image = crop_image(image, target_width, target_height)
            
            with st.container():
                # Display the image and prediction
                col1, col2, col3, col4 = st.columns([1, 4, 4, 2])
                
                with col1:
                    st.write(i+1)  # Display the row number
                    
                with col2:
                    st.image(image, use_column_width=True)
                    
                with col3:
                    c = st.container()
                    c.write(f"Hasil   :  {predicted_label}")
                    c.write(f"Tanggal :  {prediction_date.strftime('%d-%m-%Y %H:%M:%S')}")

                    
                with col4:
                    if st.button(f"Hapus", key=f"remove_{image_file}"):
                        remove_files(image_file, prediction_file) 

def crop_image(image, target_width, target_height):
    width, height = image.size
    
    # Calculate the aspect ratio
    aspect_ratio = width / height
    
    # Calculate the new dimensions with the same aspect ratio
    if aspect_ratio > 1:
        new_width = int(target_height * aspect_ratio)
        new_height = target_height
    else:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    
    # Calculate the crop box coordinates
    left = (new_width - target_width) // 2
    top = (new_height - target_height) // 2
    right = left + target_width
    bottom = top + target_height
    
    # Crop the image
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    image = image.crop((left, top, right, bottom))
    
    return image

def remove_files(image_file, prediction_file):
    if os.path.exists(image_file):
        os.remove(image_file)
    if os.path.exists(prediction_file):
        os.remove(prediction_file)


if __name__ == "__main__":
    main()

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