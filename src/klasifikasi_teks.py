import streamlit as st
import tensorflow as tf
import numpy as np
import joblib
from pathlib import Path

def classify_text(text):
    tokenizer_path = Path(__file__).parent / "model/tokenizer.joblib"
    model_path = Path(__file__).parent / "model/model_lstm.h5"

    # Memuat tokenizer dan model
    tokenizer = joblib.load(tokenizer_path)
    model = tf.keras.models.load_model(model_path)
    
    # Menyiapkan teks untuk prediksi
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=10, padding='post')
    
    # Prediksi hasil (positif/negatif)
    result = (model.predict(padded_sequences) > 0.5).astype("int32")
    return result[0][0]

def klasifikasi_teks_page():
    st.subheader("Klasifikasi Teks: Analisis Sentimen")
    
    # Input teks
    text = st.text_area("Masukkan teks yang ingin dianalisis", "")
    
    # Tambahkan tombol untuk menganalisis
    if st.button("Analisis Sentimen"):
        if text:
            with st.spinner("Memproses teks untuk prediksi..."):
                result = classify_text(text)
                classes = ["Negatif", "Positif"]
                st.subheader(f"Hasil Prediksi: **{classes[result]}**")
                st.write(f"Teks yang dianalisis: {text}")
        else:
            st.warning("Silakan masukkan teks terlebih dahulu untuk analisis!")