from ingestion.embedding_generator import EmbeddingGenerator

embedder = EmbeddingGenerator()

embedding = embedder.generate_embedding(
    "Artificial Intelligence"
)

print(type(embedding))
print()

print("Dimension:", len(embedding))
print()

print("First 10 Values:")
print(embedding[:10])