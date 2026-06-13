from ingestion.csv_loader import (
    CSVLoader
)

loader = CSVLoader()

text = loader.load(
    "data/raw/demo - Sheet1.csv"
)

print(text)