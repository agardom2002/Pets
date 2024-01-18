import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("model/pet_model.pkl")

st.title('Guess your pet!')

height = st.number_input("Height")
weight = st.number_input("Weight")
eye_color = st.selectbox("Select eye color", ("Brown", "Blue"))

if st.button('Submit'):
    x = pd.DataFrame([[height, weight, eye_color]], columns=["Height", "Weight", "Eye"])
    x = x.replace(["Brown", "Blue"], [1, 0])
    prediction = clf.predict(x)[0]
    st.text(f"This pet is a {prediction}")