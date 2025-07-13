import os
import sys
import joblib
import numpy as np
from preprocess import get_embeddings

# === 📂 PATH SETUP ===
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "feedback_model.pkl")
label_path = os.path.join(current_dir, "label_encoder.pkl")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"⚠️ Model file not found at: {model_path}")
if not os.path.exists(label_path):
    raise FileNotFoundError(f"⚠️ Label encoder file not found at: {label_path}")

model = joblib.load(model_path)
label_encoder = joblib.load(label_path)

# === 🚨 COMMON UNCLEAR ANSWERS TO BLOCK ===
UNCLEAR_RESPONSES = {
    "i don't know", "not sure", "no idea", "i am not sure", "i'm not sure",
    "i have no clue", "i don’t know", "i dunno"
}

# === 🧠 PREDICTION FUNCTION ===
def predict_response(question: str, answer: str):
    # ✅ 1. Check empty input
    if not answer.strip():
        return {
            "feedback": "Answer cannot be empty.",
            "confidence": "Low",
            "score": 0.0
        }

    # ✅ 2. Check unclear phrases directly
    answer_cleaned = answer.lower().strip()
    if answer_cleaned in UNCLEAR_RESPONSES:
        return {
            "feedback": "Your response was unclear. Please try to give a specific answer.",
            "confidence": "Low",
            "score": 0.0
        }

    # ✅ 3. Combine question + answer before embedding
    try:
        combined_input = (question + " " + answer).lower()
        embedding = get_embeddings([combined_input])
    except Exception as e:
        return {
            "feedback": f"Embedding error: {str(e)}",
            "confidence": "Low",
            "score": 0.0
        }

    # ✅ 4. Predict feedback
    try:
        predicted_label = model.predict(embedding)
        feedback = label_encoder.inverse_transform(predicted_label)[0]
    except Exception as e:
        return {
            "feedback": f"Prediction error: {str(e)}",
            "confidence": "Low",
            "score": 0.0
        }

    # ✅ 5. Confidence logic
    confidence_score = 0.75  # fallback
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(embedding)
        confidence_score = np.max(proba)

    if confidence_score >= 0.85:
        confidence_label = "High"
    elif confidence_score >= 0.6:
        confidence_label = "Medium"
    else:
        confidence_label = "Low"

    return {
        "feedback": feedback,
        "confidence": confidence_label,
        "score": round(confidence_score * 10, 2)  # scale to /10 for frontend
    }

# === ✅ LOCAL TEST ===
if __name__ == "__main__":
    question = "What is the MERN stack?"
    answer = "I don't know"
    print(predict_response(question, answer))
