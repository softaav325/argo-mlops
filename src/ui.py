import streamlit as st
import requests

st.title("🚨 ML Log Analyzer")
log_input = st.text_area("Вставьте лог сервера:", "ERROR: disk full")

import os
API_URL = os.getenv('API_URL', 'http://localhost:8000')

if st.button("Проверить"):
    try:
        response = requests.post(f"{API_URL}/predict", json={"text": log_input})
        prediction = response.json().get("prediction")
    except Exception as e:
        st.error(f"Ошибка подключения к API: {e}")
        prediction = None
    
    if prediction == "error":
        st.error(f"Результат: {prediction.upper()}")
    else:
        st.success(f"Результат: {prediction.upper()}")