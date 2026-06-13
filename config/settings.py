from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    GROQ_API_KEY: str

    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    CHROMA_PATH: str = "./chroma_db"
    COLLECTION_NAME: str = "documents"

    TOP_K: int = 10
    RERANK_TOP_K: int = 5

    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50

    CONFIDENCE_THRESHOLD: float = 0.75

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()