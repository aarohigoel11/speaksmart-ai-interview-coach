from sentence_transformers import SentenceTransformer, util

# Load your trained model
model_path = "data/model/trained_model"
model = SentenceTransformer(model_path)

# Sample sentence pairs
sentence1 = "What is the best way to learn coding?"
sentence2 = "How can I improve my programming skills?"

# Get embeddings
embeddings = model.encode([sentence1, sentence2])

# Compute cosine similarity
similarity_score = util.cos_sim(embeddings[0], embeddings[1])

print(f"Similarity Score: {similarity_score.item():.4f}")
