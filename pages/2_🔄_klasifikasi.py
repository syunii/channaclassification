import numpy as np
import torch
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.optim as optim
import io
import streamlit as st
import model

from model import ResNet
from torchvision import transforms
from torch.utils.data import DataLoader, Subset, random_split
from PIL import Image
import os



torch.manual_seed(128)

# Define the class names
class_names = ['andrao', 'asiatica', 'auranti', 'barca', 'maru', 'stewartii']

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
state_dict = torch.load('https://www.mediafire.com/file/a4uu0pbr7lujboe/resnet_modelv3.pt', map_location=device)
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

# Create the Streamlit app
def main():
    st.title("Channa Classifier")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            prediction = predict(image)
            st.write("The Picture is:", prediction)

if __name__ == "__main__":
    main()
