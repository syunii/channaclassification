import streamlit as st

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/cc.ico"
)

def main():
    st.title(":blue[Hubungi Kami]")
    st.write("jika Anda memiliki pertanyaan atau saran!")
    col1,col2,col3 = st.columns([1,30,1])
    with col1:
        st.write("")
    with col2:
        st.subheader(":blue[Informasi Kontak]")
        st.write("📧 Email : <span style='color: blue, text-align: center;'>yuniww577@gmail.com</span>",unsafe_allow_html=True)
    with col3:
        st.write("")

    st.subheader(":blue[Terimakasih telah menggunakan Channa Classification]")

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
            © 2023, Channa Classification
        </footer>
        """.format(footer_style),
        unsafe_allow_html=True
    )