from sentence_transformers import SentenceTransformer

from config.settings import settings


class EmbeddingGenerator:

    def __init__(self):

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def generate_embedding(
        self,
        text: str
    ):

        return self.model.encode(
            text,
            convert_to_numpy=True
        )

    def generate_embeddings(
        self,
        texts: list[str]
    ):

        return self.model.encode(
            texts,
            convert_to_numpy=True
        )