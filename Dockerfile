FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas scikit-learn joblib fastapi uvicorn streamlit requests

COPY src/ ./src/
COPY model.joblib . 

EXPOSE 8000
EXPOSE 8501

# По умолчанию запускаем API. Для UI команда будет переопределена в Deployment
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
