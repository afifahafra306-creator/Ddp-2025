import streamlit as st

#halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi',['luas persegi','luas segitiga','luas lingkaran'])

if menu == 'luas persegi':
    st.write('ini halaman untuk menghitung luas persegi')
    st.markdown(':red[luas persegi panjang]')
    st.image('https://i.pinimg.com/736x/e7/c4/71/e7c471d1c42adea86443237e8c3004d0.jpg',caption='gambar persegi')
    sisi = st.number_input('silahkan masukkan sisi', min_value=0,)
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')
elif menu == 'luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')
    st.markdown(':blue[luas segi tiga]')
    st.image('https://i.pinimg.com/736x/d9/5e/81/d95e81d5dad4ededc0b74e5efee50995.jpg',caption='gambar persegi tiga')
    
