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

ingestion_service = (
    IngestionService()
)


@router.post("/upload")
async def upload_document(

    file: UploadFile = File(...)

):

    try:

        file_path = (
            Path("data/uploads")
            / file.filename
        )

        contents = await file.read()

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(contents)

        result = (
            ingestion_service
            .ingest_file(
                str(file_path)
            )
        )

        return {

            "status":
                "success",

            "file":
                file.filename,

            "chunks":
                result["chunks"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )