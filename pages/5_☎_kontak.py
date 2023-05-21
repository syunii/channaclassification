import streamlit as st

def main():
    st.title("Halaman Kontak")
    st.write("Silakan hubungi kami jika Anda memiliki pertanyaan atau masukan!")

    st.subheader("Informasi Kontak")
    st.write("Email: synchronize@gmail.com.com")
    st.write("Telepon: +6285253435963")

    st.subheader("Formulir Kontak")
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
