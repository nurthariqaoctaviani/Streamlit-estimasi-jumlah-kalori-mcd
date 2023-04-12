import pickle
import streamlit as st

model = pickle.load(open('estimasi_kalori.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Kalori Makanan Di Menu McDonalds India')
st.write('---')

Protein = st.number_input('Input Protein(g)')
Total_fat = st.number_input('Input Total Lemak (g)')
Cholesterols = st.number_input('Input Cholestrol (mg)')
Total_carbohydrate = st.number_input('Input Total Karbohidrat(g)')
Total_sugars = st.number_input('Input Total Gula(g)')

predict = ''

if st.button('Estimasi Kalori'):
    predict = model.predict(
        [[Protein, Total_fat, Cholesterols, Total_carbohydrate, Total_sugars]]
    )
    st.write ('Estimasi jumlah kalori makanan di Menu McDonalds (kCal) : ', predict)