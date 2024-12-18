import streamlit as st
import tensorflow as tf
import numpy as np
from pathlib import Path
import joblib

def classify_tabular(f1, f2):
    scaler = joblib.load(Path(__file__).parent / "model/scaler.joblib")
    model = tf.keras.models.load_model(Path(__file__).parent / "model/tabular.h5")
    data = scaler.transform([[f1,f2]])
    result = (model.predict(data) > 0.5).astype("int32")
    return result[0][0]

def klasifikasi_tabular_page():
    st.subheader("Klasifikasi Data Tabular")
    
    f1 = st.slider("Fitur 1", -1.0, 2.5)
    f2 = st.slider("Fitur 2", -1.0, 1.5)
    
    if st.button("Prediksi"):
        with st.spinner("Memproses data untuk prediksi..."):
            result = classify_tabular(f1, f2)
            classes = ["Label 1", "Label 2"]
            st.subheader(f"Hasil Prediksi: **{classes[result]}**")
            st.write(f"Fitur yang dimasukkan: Fitur 1 = {f1}, Fitur 2 = {f2}")
    else:
        st.warning("Pilih nilai untuk fitur dan tekan tombol 'Prediksi'!")
