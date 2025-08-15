
import streamlit as st, re
from collections import Counter

st.title("AI Content Summarizer")
text = st.text_area("Paste article text", height=220)

def freq_summarize(text, n=3):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    words = re.findall(r'[A-Za-z]+', text.lower())
    stop = set('the a an in on at and or of to for with from by is are was were this that it as be have has had not but'.split())
    words = [w for w in words if w not in stop]
    freq = Counter(words)
    scores = []
    for s in sentences:
        sw = re.findall(r'[A-Za-z]+', s.lower())
        score = sum(freq.get(w,0) for w in sw) / (len(sw)+1e-9)
        scores.append(score)
    idx = sorted(range(len(scores)), key=lambda i: scores[i])[-n:]
    idx.sort()
    return ' '.join([sentences[i] for i in idx])

if st.button("Summarize"):
    if text.strip():
        st.write(freq_summarize(text, n=3))
    else:
        st.warning("Please paste some text.")
