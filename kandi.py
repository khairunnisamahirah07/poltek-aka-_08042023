# Library
import streamlit as st

# write
st.title('NYOBA AJA SIH KAYAK W JUGA GA PAHAM')
st.write('hello sayangku')

#INPUT
number1 = st.number_input('masukkan bilangan pertama')
st.write('bilangan pertama adalah', number1)


#INPUT
number2 = st.number_input('masukkan bilangan kedua')
st.write('bilangan kedua adalah', number2)

hasil=number1*number2
if st.button('hitung'):
    st.write(f'hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('silahkan pencet tombol hitung')
        