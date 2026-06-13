from fastapi import (
    APIRouter,
    HTTPException
)

from pydantic import BaseModel

from backend.services.rag_service import (
    RAGService
)

router = APIRouter()

rag_service = RAGService()


class ChatRequest(
    BaseModel
):

    query: str


@router.post("/chat")
async def chat(
    request: ChatRequest
):

    try:

        return (
            rag_service.chat(
                request.query
            )
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )