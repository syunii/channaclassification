import streamlit as st
import smtplib

st.set_page_config(
    page_title="Channa Classification",
    page_icon="logo/cc.ico"
)

def send_email(name, email, message):
    # Pengaturan SMTP server Gmail
    gmail_server = "smtp.gmail.com"
    port = 587  # TLS port
    
    # Ganti dengan email dan password aplikasi Anda
    sender_email = "synchronizeteam2023@gmail.com"
    password = "SADDAR2023"

    subject = "Pesan dari Channa Classification"
    body = f"Nama: {name}\nEmail: {email}\nPesan: {message}"

    try:
        # Membuat koneksi ke server
        server = smtplib.SMTP(gmail_server, port)
        server.starttls()
        
        # Login ke akun Gmail Anda
        server.login(sender_email, password)

        # Mengirim email
        server.sendmail(sender_email, "synchronizeteam2023@gmail.com", f"Subject: {subject}\n\n{body}")

        # Menutup koneksi server
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error saat mengirim email: {e}")
        return False

def main():
    st.title(":blue[Hubungi Kami]")
    st.write("jika Anda memiliki pertanyaan atau saran!")
    col1, col2, col3 = st.columns([1, 30, 1])
    with col1:
        st.write("")
    with col2:
        st.subheader(":blue[Informasi Kontak]")
        st.write("📧 Email : <span style='color: blue, text-align: center;'>synchronizeteam@gmail.com</span>",unsafe_allow_html=True)
    with col3:
        st.write("")

    st.subheader(":blue[Formulir Pertanyaan dan Saran]")
    name = st.text_input("👤 Nama")
    email = st.text_input("📧 Email")
    message = st.text_area("✉ Pesan")
    submit = st.button("📤 Kirim Pesan")

    if submit:
        if name and email and message:
            if send_email(name, email, message):
                st.success("Pesan telah terkirim! ✅")
            else:
                st.error("Terjadi kesalahan saat mengirim pesan. Silakan coba lagi nanti.")
        else:
            st.warning("Silakan isi semua field sebelum mengirim pesan.")

if __name__ == '__main__':
    main()

    # footer aplikasi
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
