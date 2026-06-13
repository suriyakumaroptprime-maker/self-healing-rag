from ingestion.pdf_loader import PDFLoader

loader = PDFLoader()

text = loader.load(
    "data/raw/sample.pdf"
)

print(text)
print(type(text))
print(len(text))