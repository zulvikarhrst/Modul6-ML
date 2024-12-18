import streamlit as st
import tensorflow as tf
import numpy as np
from pathlib import Path

def classify_image(image):
    class_names = ["Kertas", "Gunting", "Batu"]
    img = tf.keras.utils.load_img(image, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Tambah dimensi batch
    
    model_path = Path(__file__).parent / "model/model_rock_paper_scissors.h5"
    model = tf.keras.models.load_model(model_path)
    
    output = model.predict(img_array)
    score = tf.nn.softmax(output[0])
    predicted_class = class_names[np.argmax(score)]
    return predicted_class, score

def klasifikasi_citra_page():
    st.subheader("Klasifikasi Citra")
    upload = st.file_uploader("Pilih citra (jpg, jpeg, png)", type=['png', 'jpg', 'jpeg'])
    
    if upload is not None:
        st.image(upload, caption="Citra yang diunggah", use_column_width=True)
        st.spinner("Memproses citra untuk prediksi...")
        predicted_class, score = classify_image(upload)
        st.subheader(f"Prediksi: **{predicted_class}**")
        
        # Menampilkan probabilitas
        score_display = ", ".join([f"{class_name}: {score[i]*100:.2f}%" for i, class_name in enumerate(["Kertas", "Gunting", "Batu"])] )
        st.write(f"Score Kemiripan: {score_display}")
    else:
        st.warning("Silakan unggah citra terlebih dahulu!")
