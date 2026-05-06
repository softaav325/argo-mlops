import streamlit as st
import requests

st.title("🚨 ML Log Analyzer")
log_input = st.text_area("Вставьте лог сервера:", "ERROR: disk full")

if st.button("Проверить"):
    # ai-service — это имя сервиса в Kubernetes
    response = requests.post("http://ai-service/predict", json={"text": log_input})
    prediction = response.json().get("prediction")
    
    if prediction == "error":
        st.error(f"Результат: {prediction.upper()}")
    else:
        st.success(f"Результат: {prediction.upper()}")