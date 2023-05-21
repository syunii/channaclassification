import torch
import streamlit as st
import model
import uuid
import numpy as np

from model import ResNet
from torchvision import transforms
from PIL import Image, ImageGrab


st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico",
)

torch.manual_seed(128)

# Define the class names
class_names = ['Andrao', 'Asiatica', 'Auranti', 'Barca', 'Maru', 'Stewartii']

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
state_dict = torch.load('resnet_modelv3.pt', map_location=device)
model = ResNet()
model.load_state_dict(state_dict)
model = model.to(device)

# Create the predict function
def predict(image):
    image = transform(image).unsqueeze(0)
    output = model(image)
    _, predicted_idx = torch.max(output, 1)
    predicted_label = class_names[predicted_idx.item()]
    return predicted_label

# Fungsi untuk menyimpan gambar
def save_image(image, filename):
    image.save(filename)
    st.success(f"Gambar berhasil disimpan dengan nama: {filename}")


# Create the Streamlit app
def main():
    st.title("Channa Classifier")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    col1, col2 = st.columns([10,2] )
    with col1:
        predict_button = st.button("Predict")
    with col2:    
        capture_button = st.button("Capture")
        
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    
        
    if predict_button and uploaded_image is not None:
        # Lakukan prediksi gambar
        predicted_label = predict(image)
        st.info(f"Hasil prediksi: {predicted_label}")
        
    
    if capture_button:
        # Capture Screenshot
        screenshot = ImageGrab.grab()
        image = screenshot

        # Konversi gambar menjadi array NumPy
        img_array = np.array(image)

        # Tampilkan gambar hasil capture
        st.image(img_array, caption='Captured Image', use_column_width=True)

        # Membuat nama unik untuk gambar
        unique_filename = f"hasil/{uuid.uuid4().hex[:10]}.jpg"

        # Simpan gambar dengan nama otomatis
        save_image(image, unique_filename)
        st.success('Gambar berhasil disimpan dengan nama otomatis!')


    
        

# Menjalankan aplikasi utama
if __name__ == "__main__":
    main()
