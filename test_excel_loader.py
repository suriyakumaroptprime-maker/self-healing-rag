from ingestion.excel_loader import (
    ExcelLoader
)

loader = ExcelLoader()

text = loader.load(
    "data/raw/demo.xlsx"
)

print(text)