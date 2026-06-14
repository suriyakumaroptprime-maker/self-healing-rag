from pathlib import Path

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from backend.services.ingestion_service import (
    IngestionService
)

router = APIRouter()

ingestion_service = None


def get_ingestion_service():

    global ingestion_service

    if ingestion_service is None:

        ingestion_service = (
            IngestionService()
        )

    return ingestion_service


@router.post("/upload")
async def upload_document(

    file: UploadFile = File(...)

):

    try:

        file_path = (
            Path("data/uploads")
            / file.filename
        )

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        contents = await file.read()

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(contents)

        service = (
            get_ingestion_service()
        )

        result = (
            service.ingest_file(
                str(file_path)
            )
        )

        return {

            "status":
                "success",

            "file":
                file.filename,

            "chunks":
                result.get(
                    "chunks",
                    0
                )
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )