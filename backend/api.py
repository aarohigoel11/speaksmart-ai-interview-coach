from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()

    # Extract fields safely
    user_answer = data.get('answer')
    expected_answer = data.get('question')

    # Validate inputs
    if not user_answer or not expected_answer:
        return jsonify({"error": "Both 'question' and 'answer' fields are required!"}), 400

    # Encode and compute similarity
    embeddings = model.encode([user_answer, expected_answer], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()

    feedback = "Excellent answer!" if similarity > 0.85 else "Good attempt, but try to be more precise."

    return jsonify({
        "similarity_score": round(similarity, 2),
        "feedback": feedback,
        "confidence": "High" if similarity > 0.75 else "Medium" if similarity > 0.5 else "Low"
    })

if __name__ == '__main__':
    app.run(debug=True)
