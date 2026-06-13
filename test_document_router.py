from ingestion.document_router import (
    DocumentRouter
)

router = DocumentRouter()

text = router.load_document(
    "data/raw/demo.xlsx"
)

print(text[:500])