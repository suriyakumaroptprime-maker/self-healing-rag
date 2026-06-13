from ingestion.image_loader import (
    ImageLoader
)

loader = ImageLoader()

text = loader.load(
    "data/raw/data analyst free resorces.png"
)

print(text)