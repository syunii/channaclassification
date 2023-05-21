import streamlit as st
import os
from PIL import Image

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico",
)

# Path to the image folder
image_folder = "hasil"

# Get the list of image file names in the folder sorted by creation time
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.endswith((".jpg", ".jpeg", ".png"))],
    key=lambda f: os.path.getctime(os.path.join(image_folder, f)),
    reverse=True,
)

# Display the Streamlit page
def main():
    st.title("Galeri Hasil Test")
    
    if len(image_files) == 0:
        st.warning("Tidak ada gambar dalam folder.")
    else:
        st.write(f"Jumlah gambar: {len(image_files)}")
        
        # Calculate the target size for cropping
        target_width = 600
        target_height = 300
        
        # Loop through each image file in the folder
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            image = Image.open(image_path)
            prediction_path = os.path.splitext(image_path)[0] + ".txt"
            if os.path.exists(prediction_path):
                with open(prediction_path, "r") as f:
                    predicted_label = f.read()
            else:
                predicted_label = "Prediksi tidak tersedia"
            
            # Crop the image to have the target dimensions
            image = crop_image(image, target_width, target_height)
            
            # Display the image and prediction
            col1, col2 = st.columns([10, 1])
            
            with col1:
                st.image(image, caption=image_file, use_column_width=False)
                st.info(f"Hasil prediksi: {predicted_label}")
            
            with col2:
                if st.button(f"❌", key=f"remove_{image_file}"):
                    os.remove(image_path)
                    # Update the image file list after deletion
                    image_files.remove(image_file)
                    # Remove the prediction file if exists
                    if os.path.exists(prediction_path):
                        os.remove(prediction_path)

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

if __name__ == "__main__":
    main()
