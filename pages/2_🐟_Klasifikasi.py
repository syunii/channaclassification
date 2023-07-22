import torch
import streamlit as st
import uuid
import os

from torchvision import transforms
from PIL import Image
from modeltrained import ResNet18
from rekomendasi import andrao, asiatica, auranti, barca, bukan_channa, limbata, maru, stewartii

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/cc.ico"
)

torch.manual_seed(128)
# Define the class names
class_names = ['Andrao', 'Asiatica', 'Auranti', 'Barca', 'Bukan Channa', 'Limbata', 'Maru', 'Stewartii']

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
state_dict = torch.load('ResNet18New2.pt', map_location=device)
model = ResNet18()
model.load_state_dict(state_dict)
model = model.to(device)
model.eval()

# Create the predict function
def predict(image):
    image = transform(image).unsqueeze(0)
    output = model(image)
    _, predicted_idx = torch.max(output, 1)
    predicted_label = class_names[predicted_idx.item()]
    return predicted_label

# Function to save the image, prediction results, and accuracy
def save_result(image, predicted_label):
    unique_filename = f"hasil/{uuid.uuid4().hex[:10]}"
    save_image(image, f"{unique_filename}.jpg")
    save_prediction(predicted_label, f"{unique_filename}.txt")

# Function to save the image
def save_image(image, filename):
    image.save(filename)

# Function to save the prediction result to a file
def save_prediction(predicted_label, filename):
    with open(filename, "w") as f:
        f.write(f"\n{predicted_label}")

# Function to display the image and prediction
def show_prediction(predicted_label):
    st.info(f"Hasil prediksi: {predicted_label}")

# Create the Streamlit app
def main():
    st.title(":orange[Klasifikasi]")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        resized_image = Image.open(uploaded_image)
        image = resized_image.resize((256, 256))  # Atur ukuran gambar menggunakan transformasi PIL
        st.image(image,  use_column_width=True)  # Tampilkan gambar yang diunggah dengan lebar kolom konten
        if st.button("Predict"):
            # Perform image prediction
            predicted_label = predict(image)
            show_prediction(predicted_label)
            st.success(f"Prediksi Berhasil!")
            save_result(image, predicted_label)
            if predicted_label == "Andrao":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)
                andrao(predicted_label)
            elif predicted_label == "Asiatica":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)
                asiatica(predicted_label)
            elif predicted_label == "Auranti":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)
                auranti(predicted_label)
            elif predicted_label == "Barca":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)
                barca(predicted_label)
            elif predicted_label == "Bukan Channa":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)
                barca(predicted_label)
            elif predicted_label == "Limbata":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)
                barca(predicted_label)
            elif predicted_label == "Maru":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)               
                maru(predicted_label)
            elif predicted_label == "Stewartii":
                st.write("<h2 style='text-align: center; color: orange;'>Rekomendasi toko</h2>", unsafe_allow_html=True)             
                stewartii(predicted_label)
            else:
                st.info(f"Hasil prediksi: Tidak diketahui")
          

# Create the "hasil" folder if it doesn't exist
if not os.path.exists("hasil"):
    os.makedirs("hasil")

# Run the main application
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

