from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("data/model/trained_model")

def get_similarity(sentence1, sentence2):
    embeddings = model.encode([sentence1, sentence2])
    score = util.cos_sim(embeddings[0], embeddings[1])
    return score.item()
