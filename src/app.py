from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

# Load model and vectorizer
MODEL_PATH = 'model.joblib'
if os.path.exists(MODEL_PATH):
    artifacts = joblib.load(MODEL_PATH)
    model = artifacts['model']
    vectorizer = artifacts['vectorizer']
else:
    model = None
    vectorizer = None

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "AI Service is running"}

@app.post("/predict")
def predict(request: TextRequest):
    if model is None or vectorizer is None:
        return {"error": "Model not loaded"}
    
    vec_text = vectorizer.transform([request.text])
    prediction = model.predict(vec_text)[0]
    label = "error" if prediction == 1 else "info"
    
    return {"prediction": label}
