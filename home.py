import streamlit as st
from PIL import Image
from datetime import date

# Inisialisasi total kunjungan
if 'total_visits' not in st.session_state:
    st.session_state['total_visits'] = 0

# Menaikkan total kunjungan
st.session_state.total_visits += 1

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico",
)

col1, col2 = st.columns([10,3])
with col1:
    # Menampilkan tanggal
    current_date = date.today().strftime("%B %d, %Y")
    st.write("Today's date is:", current_date)
with col2:
    # Menampilkan total kunjungan
    st.write("Total Kunjungan:", st.session_state.total_visits)
    
# Title and introduction
st.markdown(
    """
    <h1 style='text-align: center;'>Channa Fish Classification Dashboard</h1>
    <p style='text-align: center;'>Welcome to the Fish Classification Dashboard!</p>
    <style>
    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([10,10,10])

with col1:
    st.write(' ')

with col2:
    st.image("logo/android-chrome-512x512.png", caption='Channa Classification Logo', width=250)

with col3:
    st.write(' ')



# Home page content
st.header("Home Page")
st.write("This is the Home page of the Channa Fish Classification Dashboard. Here, you can find information about Channa fish and get started with the classification.")

# Information about Channa fish
st.subheader("About Channa Fish")
st.write("Channa fish, also known as snakehead fish, are freshwater predatory fish found in Asia and Africa. They are known for their aggressive behavior and can survive in various habitats.")

# Getting started with classification
st.subheader("Getting Started with Classification")
st.write("To classify an image as a Channa fish or not, navigate to the 'Image Classification' page from the sidebar. Upload an image and let the classification model determine if it's a Channa fish.")


