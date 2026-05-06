import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib

def train_model():
    # Load data
    df = pd.read_csv('/app/data/dataset.csv')
    
    # Preprocessing
    X = df['text']
    y = df['label'].map({'info': 0, 'error': 1})
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Vectorization
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Model
    model = LogisticRegression()
    model.fit(X_train_vec, y_train)
    
    # Evaluation
    predictions = model.predict(X_test_vec)
    acc = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    
    print(f"Model Training Complete.")
    print(f"Accuracy: {acc:.4f}")
    print(f"F1 Score: {f1:.4f}")
    
    # Save model and vectorizer
    joblib.dump({'model': model, 'vectorizer': vectorizer}, '/app/data/model.joblib')
    print("Model saved to /app/data/model.joblib")

if __name__ == "__main__":
    train_model()
