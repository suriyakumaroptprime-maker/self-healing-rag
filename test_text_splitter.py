from ingestion.pdf_loader import PDFLoader
from ingestion.text_splitter import TextSplitter

loader = PDFLoader()
splitter = TextSplitter()

text = loader.load("data/raw/sample.pdf")

chunks = splitter.split(text)

print("Total Chunks:", len(chunks))
print("\nFirst Chunk:\n")
print(chunks[0])