import os
import streamlit as st
import pandas as pd
import matplotlib
import numpy as np
from joblib import load

# Menampilkan versi modul yang digunakan
st.write("pandas version:", pd.__version__)
st.write("matplotlib version:", matplotlib.__version__)
st.write("numpy version:", np.__version__)

# Menggunakan try-except untuk impor sklearn dan menampilkan pesan yang jelas
try:
    import sklearn
    st.write("scikit-learn version:", sklearn.__version__)
except ModuleNotFoundError:
    st.write("scikit-learn is not installed. Please check the requirements.txt file.")

current_path = os.getcwd()
st.write(f"Current working directory: {current_path}")

file_path = os.path.join(current_path, 'diabetes_model.pkl')
st.write(f"Trying to open file at: {file_path}")

if os.path.exists(file_path):
    st.write("File found, loading the model...")
    # Coba memuat model menggunakan joblib
    try:
        diabetes_model = load(file_path)
    except:
        diabetes_model = pickle.load(open(file_path, 'rb'))
else:
    st.write("File not found, please check the path and file name.")
    
#membaca model 
#diabetes_model = pickle.load(open('Diabetes prediction/diabetes_model.pkl', 'rb'))

#judul web 
st.title('Diabetes Prediction')

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input("Pregnancies", placeholder="Masukkan jumlah kehamilan")

with col2:
    Glucose = st.text_input("Glucose", placeholder="Masukkan kadar glukosa")

with col1:
    BloodPressure = st.text_input("Blood Pressure", placeholder="Masukkan tekanan darah")

with col2:
    SkinThickness = st.text_input("Skin Thickness", placeholder="Masukkan ketebalan kulit")

with col1:
    Insulin = st.text_input("Insulin", placeholder="Masukkan kadar insulin")

with col2:
    BMI = st.text_input("BMI", placeholder="Masukkan BMI")

with col1:
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function", placeholder="Masukkan fungsi pedigree diabetes")

with col2:
    Age = st.text_input("Age", placeholder="Masukkan usia")

# Validasi dan konversi input
def validasi_input(value, tipe):
    if value.strip() == "":
        return None
    try:
        return tipe(value)
    except ValueError:
        return None

Pregnancies = validasi_input(Pregnancies, int)
Glucose = validasi_input(Glucose, int)
BloodPressure = validasi_input(BloodPressure, int)
SkinThickness = validasi_input(SkinThickness, int)
Insulin = validasi_input(Insulin, int)
BMI = validasi_input(BMI, float)
DiabetesPedigreeFunction = validasi_input(DiabetesPedigreeFunction, float)
Age = validasi_input(Age, int)

#kode untuk prediksi
diabetes_diagnosis = ''

if st.button("Predict"):
    # Periksa apakah ada input kosong atau tidak valid
    if None in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]:
        st.error("Harap isi semua input dengan nilai yang valid.")
    else:
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diabetes_prediction[0] == 1:
            st.success("Pasien terkena diabetes.")
        else:
            st.success("Pasien tidak diabetes.")
