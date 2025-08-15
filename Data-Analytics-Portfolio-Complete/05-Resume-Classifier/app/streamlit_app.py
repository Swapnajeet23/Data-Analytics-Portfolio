
import streamlit as st, joblib
from pathlib import Path
import pandas as pd

st.title("Resume Classification (TF-IDF + Logistic Regression)")
st.write("Paste resume text and classify into predefined roles.")

@st.cache_resource
def load():
    import joblib
    tf = joblib.load(Path(__file__).parent.parent/'data'/'tfidf.joblib')
    clf = joblib.load(Path(__file__).parent.parent/'data'/'logreg.joblib')
    return tf, clf

text = st.text_area("Resume text", height=200)
if st.button("Classify"):
    tf, clf = load()
    X = tf.transform([text])
    pred = clf.predict(X)[0]
    st.success(f"Predicted role: {pred}")
