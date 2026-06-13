from config.settings import settings

print("Model:", settings.GROQ_MODEL)
print("Top K:", settings.TOP_K)
print("Chunk Size:", settings.CHUNK_SIZE)
print("Collection:", settings.COLLECTION_NAME)
print("Confidence:", settings.CONFIDENCE_THRESHOLD)