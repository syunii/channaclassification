import streamlit as st

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/favicon.ico"
)

def main():
    st.title(":orange[Halaman Kontak]")
    st.write("Silakan hubungi kami jika Anda memiliki pertanyaan atau masukan!")
    col1,col2,col3 = st.columns([1,30,1])
    with col1:
        st.write("")
    with col2:
        st.subheader(":orange[Informasi Kontak]")
        st.write("Email: <span style='color: blue, text-align: center;'>synchronize@gmail.com</span>",unsafe_allow_html=True)
        st.write("Telepon: <span style='color: green;'>+6285253435963</span>", unsafe_allow_html=True)
    with col3:
        st.write("")
    


    st.subheader(":orange[Formulir Kontak]")
    name = st.text_input("Nama")
    email = st.text_input("Email")
    message = st.text_area("Pesan")
    submit = st.button("Kirim Pesan")

    if submit:
        # Proses pengiriman pesan
        # Misalnya, kirim email atau simpan pesan ke database
        st.success("Pesan telah terkirim!")

if __name__ == '__main__':
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
            © 2023, Synchronize Team
        </footer>
        """.format(footer_style),
        unsafe_allow_html=True
    )