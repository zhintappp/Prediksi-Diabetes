import pickle 
import streamlit as st 

#membaca model 
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))

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
