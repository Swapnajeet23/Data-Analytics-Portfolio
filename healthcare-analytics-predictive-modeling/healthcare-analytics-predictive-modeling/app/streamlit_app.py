
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Healthcare Risk Prediction", layout="centered")
st.title("🏥 Healthcare Risk Prediction (Offline)")

MODEL_PATH = Path("models/best_model.joblib")
if not MODEL_PATH.exists():
    st.error("Model file not found. Please run the training notebook to generate it.")
    st.stop()

pipe = joblib.load(MODEL_PATH)

st.markdown("Enter patient information to predict heart-disease risk.")

cols = st.columns(3)
age = cols[0].number_input("Age", 18, 100, 54)
sex = cols[1].selectbox("Sex (1=Male, 0=Female)", [1,0], index=0)
cp = cols[2].selectbox("Chest Pain Type (0-3)", [0,1,2,3], index=0)

cols2 = st.columns(3)
trestbps = cols2[0].number_input("Resting BP", 80, 220, 130)
chol = cols2[1].number_input("Cholesterol", 100, 600, 246)
fbs = cols2[2].selectbox("Fasting Blood Sugar > 120 (1/0)", [0,1], index=0)

cols3 = st.columns(3)
restecg = cols3[0].selectbox("Resting ECG (0-2)", [0,1,2], index=0)
thalach = cols3[1].number_input("Max Heart Rate", 60, 220, 150)
exang = cols3[2].selectbox("Exercise Induced Angina (1/0)", [0,1], index=0)

cols4 = st.columns(3)
oldpeak = cols4[0].number_input("ST Depression (oldpeak)", 0.0, 6.5, 1.0, step=0.1)
slope = cols4[1].selectbox("Slope (0-2)", [0,1,2], index=0)
ca = cols4[2].selectbox("Number of Vessels (0-3)", [0,1,2,3], index=0)

thal = st.selectbox("Thalassemia (1=normal,2=fixed defect,3=reversible defect)", [1,2,3], index=1)

if st.button("Predict Risk"):
    row = pd.DataFrame([{
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps, "chol": chol,
        "fbs": fbs, "restecg": restecg, "thalach": thalach, "exang": exang,
        "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }])
    proba = pipe.predict_proba(row)[0,1]
    label = "High Risk" if proba>=0.5 else "Low Risk"
    st.subheader(f"Prediction: {label}")
    st.metric("Probability of risk", f"{proba*100:.1f}%")
    st.caption("Model: best of Logistic Regression, Random Forest, GradientBoosting (trained offline).")
