import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt


# Membuat sidebar
with st.sidebar:
    sidebar = st.sidebar.selectbox("Navigasi", ("Home", "Car Price","Bar","About"))
if sidebar == "Home":
    import streamlit as st
    st.title("My Self")
    nama = "Hanum Tyas Nurani"
    st.write("Halo, nama saya adalah {}.".format(nama),"saya berasal dari kabupaten ngawi provinsi jawa timur ")
    # Foto
    image_url = "hanum.jpg"
    st.image(image_url, width=300)


    # Alamat email
    email = "hanumtyas2004@gmail.com"
    st.write("Alamat email : {}".format(email))

    # Nomor telepon
    telepon = "+6282229020694"
    st.write("Nomor telepon : {}".format(telepon))

    # Link ke media sosial
    instagram = "https://www.instagran.com/hanumtyas_"
    whatsapp = "https://wa.me/+6282229020694"
    st.write("Link ke media sosial:")
    st.write("* Instagram : {}".format(instagram))
    st.write("* Whatsapp : {}".format(whatsapp))
elif sidebar == "Car Price":
    model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))
    st.title('Car Price Prediction')
    st.header("Dataset")
    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)

    st.write("Grafik Highway-mpg")
    chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
    st.line_chart(chart_highwaympg)

    st.write("Grafik curbweight")
    chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
    st.line_chart(chart_curbweight)

    st.write("Grafik horsepower")
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)

    highwaympg = st.number_input('Highway-mpg', 0, 10000000)
    curbweight = st.number_input('Curbweight', 0, 10000000)
    horsepower = st.number_input('Horsepower', 0, 10000000)

    if st.button('Prediksi'):
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])

        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: $ {harga_mobil_formatted}')
elif sidebar == "Bar":
    st.markdown("<h1 style='text-align: center;'>Menampilkan Bar</h1>", unsafe_allow_html=True)
    df  = pd.DataFrame(
        np.random.randn(10,2),
        columns=['x','y']
    )
    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)
elif sidebar == "About":
    st.markdown("<h1 style='text-align: center;'>About Page</h1>", unsafe_allow_html=True)
    st.subheader("Streamlit Aplication")
    st.image('logo.svg')
    # Buka file txt
    with open("deskripsi.txt", "r") as f:
        # Baca isi file
        data = f.read()

    # Tampilkan isi file
    st.write(data)

