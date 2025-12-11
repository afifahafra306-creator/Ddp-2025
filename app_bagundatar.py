import streamlit as st
# Fungsi untuk menghitung luas bangun datar
def persegi(sisi):
    return sisi * sisi

def segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def lingkaran(jari2):
    return 3.14 * jari2 * jari2

def persegi_panjang(panjang, lebar):
    return panjang * lebar

def jajar_genjang(alas, tinggi):
    return alas * tinggi

# Halaman Utama
st.title('Aplikasi Perhitungan Luas Bangun Datar')
st.title('Buatan anak SI')

# Sidebar navigasi
menu = st.sidebar.selectbox('Menu', ['Luas Persegi', 'Luas Segitiga', 'Luas Lingkaran', 'Luas Persegi Panjang', 'Luas Jajar Genjang' ])

if menu == 'Luas Persegi':
    st.subheader('Hitung Luas Persegi')

    # Menampilkan gambar ilustrasi
    st.image(
        "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQ4dJ9QMK_50OUPJNELw3AbynuL1f33ESOSq_nlFi-gnMIA4SMDvJ8Vy39NcxfWGqlv2Bn6EiIFlGm2rLw4xxmYTMD3wL85mgXggy86WRuR02OYSCKWbCIUyjOI88dCwKMctfLj3txfNM/s1600/rumus-luas-persegi-dan-keliling-persegi.JPG",
        caption="Ilustrasi Persegi",
        width=300,
    )

    # Input sisi
    input_sisi = st.number_input('silahkan Masukkan Sisi', min_value=0)
    if st.button('Hitung Luas Persegi'):
        if input_sisi > 0:
            luas = persegi(input_sisi)
            st.write(f"Luas persegi adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai sisi yang lebih besar dari 0!')

elif menu == 'Luas Segitiga':
    st.subheader('Hitung Luas Segitiga')

    # Menampilkan gambar ilustrasi
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvnU93yw54EG4p3cL7lMuWFeCGlkPv0co7cA&s",
        caption="Ilustrasi Segitiga",
        width=300,
    )

    # Input Data
    input_alas = st.number_input('Masukkan Alas', min_value=0.0)
    input_tinggi = st.number_input('Masukkan Tinggi', min_value=0.0)

    if st.button('Hitung Luas Segitiga'):
        if input_alas > 0 and input_tinggi > 0:
            luas = segitiga(input_alas, input_tinggi)
            st.write(f"Luas segitiga adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai alas dan tinggi yang lebih besar dari 0!')

elif menu == 'Luas Lingkaran':
    st.subheader('Hitung Luas Lingkaran')

    # Menampilkan gambar ilustrasi
    st.image(
        "https://thumb.viva.co.id/media/frontend/thumbs3/2022/04/11/6253bd91b52f8-rumus-luas-lingkaran_1265_711.jpg",
        caption="Ilustrasi Lingkaran",
        width=300,
    )

    # Input Data
    input_jari2 = st.number_input('Masukkan Jari-Jari', min_value=0.0)

    if st.button('Hitung Luas Lingkaran'):
        if input_jari2 > 0:
            luas = lingkaran(input_jari2)
            st.write(f"Luas lingkaran adalah: {luas:.2f}")
        else:
            st.warning('Masukkan nilai jari-jari yang lebih besar dari 0!')

elif menu == 'Luas Persegi Panjang':
    st.subheader('Hitung Luas Persegi Panjang')
    st.image(
        "data:image/png;base64,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",
        width=300,
        caption="Ilustrasi Persegi Panjang"
    )

    panjang = st.number_input('Masukkan Panjang', min_value=0.0)
    lebar = st.number_input('Masukkan Lebar', min_value=0.0)

    if st.button('Hitung Luas Persegi Panjang'):
        if panjang > 0 and lebar > 0:
            st.success(f"Luas persegi panjang adalah: {persegi_panjang(panjang, lebar):.2f}")
        else:
            st.warning('Masukkan panjang dan lebar > 0!')

# --- Jajar Genjang ---
elif menu == 'Luas Jajar Genjang':
    st.subheader('Hitung Luas Jajar Genjang')
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlUQeZTKwvwyrUKcSqhEiN3MPoDgWExY_nWw&s",
        caption="Ilustrasi Jajar Genjang",
        width=300
    )

    alas = st.number_input('Masukkan Alas', min_value=0.0)
    tinggi = st.number_input('Masukkan Tinggi', min_value=0.0)

    if st.button('Hitung Luas Jajar Genjang'):
        if alas > 0 and tinggi > 0:
            st.success(f"Luas jajar genjang adalah: {jajar_genjang(alas, tinggi):.2f}")
        else:
            st.warning('Masukkan alas dan tinggi > 0!')