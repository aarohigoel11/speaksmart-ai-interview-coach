import os
import sys
import subprocess
from flask import Flask, render_template, request, jsonify
import random
import csv
import speech_recognition as sr
from pydub import AudioSegment

# 👇 Add this line
os.environ["PATH"] += os.pathsep + r"C:\Users\aaroh\OneDrive\Desktop\My web dev notes\SpeakSmart\ffmpeg-7.1.1-full_build (1)\ffmpeg-7.1.1-full_build\bin"

# 👇 Then keep this inside process_answer function before using AudioSegment

AudioSegment.ffmpeg = r"C:\Users\aaroh\OneDrive\Desktop\My web dev notes\SpeakSmart\ffmpeg-7.1.1-full_build (1)\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"




# ✅ Load ML model
sys.path.append(os.path.abspath("../ml-model/data/model"))
from inference import predict_response

app = Flask(__name__)

# ✅ Load questions from dataset
CSV_PATH = r"C:\Users\aaroh\OneDrive\Desktop\My web dev notes\SpeakSmart\data\speaksmartdataset.csv"

def load_questions():
    questions = []
    with open(CSV_PATH, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get("Question"):
                questions.append(row["Question"])
    return questions

questions_list = load_questions()

# ✅ Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-question')
def get_question():
    if not questions_list:
        return jsonify({"error": "No questions found in CSV."}), 500
    return jsonify({"question": random.choice(questions_list)})

@app.route('/process-answer', methods=['POST'])
def process_answer():
    audio = request.files.get('audio')
    question = request.form.get('question')

    if not audio or not question:
        return jsonify({"error": "Missing audio or question."}), 400

    # 🔃 Save temporary audio files
    webm_path = "temp.webm"
    wav_path = "temp.wav"
    audio.save(webm_path)

    try:
        # 🔄 Convert .webm to .wav using ffmpeg via pydub
        sound = AudioSegment.from_file(webm_path)
        sound.export(wav_path, format="wav")

        # 🎤 Speech-to-text
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            user_answer = recognizer.recognize_google(audio_data)

    except Exception as e:
        print("🔴 Audio processing error:", e)
        user_answer = "Could not process audio"

    finally:
        # 🧹 Cleanup
        if os.path.exists(webm_path): os.remove(webm_path)
        if os.path.exists(wav_path): os.remove(wav_path)

    # ❗ If recognition fails, skip ML prediction
    if "Could not" in user_answer:
        return jsonify({
            "answer": user_answer,
            "feedback": "Unable to evaluate due to unclear audio.",
            "confidence": "Low",
            "score": 0
        })

    # 🧠 ML model feedback
    result = predict_response(question, user_answer)

    return jsonify({
        "answer": user_answer,
        "feedback": result.get("feedback", "No feedback"),
        "confidence": result.get("confidence", "N/A"),
        "score": result.get("score", 0)
    })

# ✅ Run server
if __name__ == '__main__':
    app.run(debug=True)
