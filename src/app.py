import streamlit as st
from klasifikasi_teks import klasifikasi_teks_page
from klasifikasi_citra import klasifikasi_citra_page
from klasifikasi_tabular import klasifikasi_tabular_page

# Set judul aplikasi
st.set_page_config(page_title="Aplikasi Klasifikasi", layout="wide")
st.title("Aplikasi Klasifikasi - Teks, Citra, dan Tabular")

# Sidebar untuk navigasi
st.sidebar.title("Pilih Halaman")
page = st.sidebar.radio("Pilih Halaman", ["Home", "Klasifikasi Teks", "Klasifikasi Citra", "Klasifikasi Tabular"])

# Home Page
if page == "Home":
    st.subheader("Selamat datang di Aplikasi Klasifikasi")
    st.write("""
    Aplikasi ini memungkinkan Anda untuk melakukan klasifikasi pada tiga jenis data:
    - **Teks**: Menganalisis sentimen teks sebagai positif atau negatif.
    - **Citra**: Mengklasifikasikan gambar menjadi salah satu dari beberapa kelas.
    - **Tabular**: Menganalisis data tabular untuk mengklasifikasikan berdasarkan fitur yang diberikan.

    Pilih salah satu kategori klasifikasi pada sidebar untuk memulai.
    """)

    st.write("### Informasi Pengguna")
    st.write("**Nama**: Zulvikar Harist")
    st.write("**NIM**: 202110370311033")
    st.write("**Deskripsi**: Aplikasi ini dibuat untuk membantu dalam analisis klasifikasi menggunakan model pembelajaran mesin pada data teks, citra, dan tabular.")

# Menampilkan halaman klasifikasi berdasarkan tab yang dipilih
elif page == "Klasifikasi Teks":
    klasifikasi_teks_page()
elif page == "Klasifikasi Citra":
    klasifikasi_citra_page()
elif page == "Klasifikasi Tabular":
    klasifikasi_tabular_page()

# Footer
st.markdown(f"""
    ---  
    <p style="font-size:12px; text-align:center;">
    Dibuat oleh: Zulvikar Harist | NIM: 202110370311033 | <a href="https://github.com/zulvikarhrst" target="_blank">GitHub</a>
    </p>
""", unsafe_allow_html=True)