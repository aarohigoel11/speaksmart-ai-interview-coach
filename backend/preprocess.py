from sentence_transformers import SentenceTransformer

# Load the model once
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(sentences):
    return embedder.encode(sentences)
