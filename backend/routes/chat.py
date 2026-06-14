from fastapi import (
    APIRouter,
    HTTPException
)

from pydantic import BaseModel

from backend.services.rag_service import (
    RAGService
)

router = APIRouter()

rag_service = None


def get_rag_service():

    global rag_service

    if rag_service is None:

        rag_service = RAGService()

    return rag_service


class ChatRequest(
    BaseModel
):

    query: str


@router.post("/chat")
async def chat(
    request: ChatRequest
):

    try:

        service = get_rag_service()

        return service.chat(
            request.query
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )