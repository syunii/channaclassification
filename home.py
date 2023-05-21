import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Channa Classification",
    page_icon="https://www.mediafire.com/file/1osnnszkwrjao0q/favicon.ico",
)
# Title and introduction
st.title("Channa Fish Classification Dashboard")
st.write("Welcome to the Channa Fish Classification Dashboard!")
st.image("https://www.mediafire.com/view/b9zdx2c8zsa594r/android-chrome-512x512.png")

# Home page content
st.header("Home Page")
st.write("This is the Home page of the Channa Fish Classification Dashboard. Here, you can find information about Channa fish and get started with the classification.")

# Information about Channa fish
st.subheader("About Channa Fish")
st.write("Channa fish, also known as snakehead fish, are freshwater predatory fish found in Asia and Africa. They are known for their aggressive behavior and can survive in various habitats.")

# Getting started with classification
st.subheader("Getting Started with Classification")
st.write("To classify an image as a Channa fish or not, navigate to the 'Image Classification' page from the sidebar. Upload an image and let the classification model determine if it's a Channa fish.")
