import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from preprocess import get_embeddings  # ✅ Make sure this works

# === ✅ Load the Dataset ===
file_path = r"C:\Users\aaroh\OneDrive\Desktop\My web dev notes\SpeakSmart\data\speaksmartdataset_final.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Dataset not found at: {file_path}")

df = pd.read_csv(file_path)

# === 🔍 Validate Columns ===
if "Answer" not in df.columns or "Feedback" not in df.columns:
    raise ValueError("CSV must contain 'Answer' and 'Feedback' columns")

# === 📈 Prepare Data ===
X = get_embeddings(df["Answer"].tolist())  # ➤ Convert answers to embeddings

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df["Feedback"])  # ➤ Encode feedback

# === 🏋️ Train Logistic Regression Model ===
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# === 💾 Save Model & Encoder ===
save_dir = os.path.dirname(__file__)
joblib.dump(model, os.path.join(save_dir, "feedback_model.pkl"))
joblib.dump(label_encoder, os.path.join(save_dir, "label_encoder.pkl"))

print("✅ Training complete. Model & encoder saved.")
