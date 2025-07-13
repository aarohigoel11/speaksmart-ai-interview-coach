<h1 align="center">🎤 SpeakSmart Interview</h1>
<p align="center">
  <b>Practice. Analyze. Improve.</b><br>
  An AI-powered mock interview platform for real-time technical speaking evaluation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blueviolet" />
  <img src="https://img.shields.io/badge/Built%20With-Flask-blue" />
  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%20%7C%20JS-orange" />
</p>

---

## ✨ Features

- 🎙️ Real-time voice input via mic
- 🤖 Auto-generated technical questions
- 🧠 Natural language understanding for response analysis
- 📊 Instant scoring, confidence & feedback
- 👩‍💻 Webcam support to simulate real interviews

---

## 🧠 ML/NLP Pipeline Overview

| Stage            | Tool/Technique                             | Description                                     |
|------------------|--------------------------------------------|-------------------------------------------------|
| 🎤 Voice Input   | WebRTC / MediaRecorder API                 | Capture candidate response                     |
| 📄 Transcription | SpeechRecognition / Web Speech API         | Convert speech to text                         |
| 🔍 NLP Analysis  | Custom ML model or OpenAI API              | Analyze content clarity, keywords, and intent  |
| 📈 Scoring       | Rule-based + ML scoring model              | Generate score, confidence & feedback          |

---

## 🧰 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%20%7C%20JavaScript-informational?logo=javascript" />
  <img src="https://img.shields.io/badge/Backend-Flask-lightgrey?logo=python" />
  <img src="https://img.shields.io/badge/ML-NLP%20%7C%20Scikit--Learn-yellow?logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Recording-WebRTC%20%7C%20MediaRecorder-orange?logo=webrtc" />
  <img src="https://img.shields.io/badge/Model%20Storage-Joblib-green?logo=python" />
  <img src="https://img.shields.io/badge/UI-Responsive-green?logo=bootstrap" />
</p>

---

## 📸 Screenshots

### 💻 Interview UI
<img src="./Screenshot 2025-07-13 170807.png" width="80%" alt="Interview UI Screenshot" />

### 📊 Response Analysis
<img src="./Screenshot 2025-07-13 165811.png" width="60%" alt="Score Example 1" />



---

## 🛠️ Installation Guide

```bash
# 1. Clone the repository
git clone https://github.com/your-username/speaksmart.git
cd speaksmart

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask server
python app.py
