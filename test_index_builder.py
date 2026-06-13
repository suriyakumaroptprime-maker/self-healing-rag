from ingestion.index_builder import (
    IndexBuilder
)

builder = IndexBuilder()

result = builder.index_document(
    "data/raw/sample.pdf"
)

print(result)