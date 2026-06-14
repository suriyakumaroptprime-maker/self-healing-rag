from sentence_transformers import SentenceTransformer

from config.settings import settings


class EmbeddingGenerator:

    def __init__(self):

        self.model = None

    def get_model(self):

        if self.model is None:

            self.model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

        return self.model

    def generate_embedding(
        self,
        text: str
    ):

        model = self.get_model()

        return model.encode(
            text,
            convert_to_numpy=True
        )

    def generate_embeddings(
        self,
        texts: list[str]
    ):

        model = self.get_model()

        return model.encode(
            texts,
            convert_to_numpy=True
        )