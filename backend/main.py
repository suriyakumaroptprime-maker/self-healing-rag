from fastapi import FastAPI

from backend.routes.upload import (
    router as upload_router
)

from backend.routes.chat import (
    router as chat_router
)

app = FastAPI(

    title="Self-Healing RAG API",

    version="1.0.0"
)

app.include_router(
    upload_router
)

app.include_router(
    chat_router
)


@app.get("/")
def home():

    return {

        "message":
        "Self-Healing RAG API Running"
    }


@app.get("/health")
def health():

    return {

        "status":
        "healthy"
    }