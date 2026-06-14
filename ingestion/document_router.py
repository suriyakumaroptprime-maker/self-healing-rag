from ingestion.pdf_loader import PDFLoader
from ingestion.csv_loader import CSVLoader
from ingestion.excel_loader import ExcelLoader

try:

    from ingestion.image_loader import ImageLoader

except Exception:

    ImageLoader = None


class DocumentRouter:

    def __init__(self):

        self.pdf_loader = PDFLoader()

        self.csv_loader = CSVLoader()

        self.excel_loader = ExcelLoader()

        self.image_loader = None

        if ImageLoader is not None:

            self.image_loader = ImageLoader()

    def load_document(
        self,
        file_path: str
    ):

        file_path = file_path.lower()

        if file_path.endswith(".pdf"):

            return self.pdf_loader.load(
                file_path
            )

        elif file_path.endswith(".csv"):

            return self.csv_loader.load(
                file_path
            )

        elif (
            file_path.endswith(".xlsx")
            or
            file_path.endswith(".xls")
        ):

            return self.excel_loader.load(
                file_path
            )

        elif (
            file_path.endswith(".png")
            or
            file_path.endswith(".jpg")
            or
            file_path.endswith(".jpeg")
        ):

            if self.image_loader is None:

                raise ValueError(
                    "OCR support is disabled in deployment."
                )

            return self.image_loader.load(
                file_path
            )

        else:

            raise ValueError(
                f"Unsupported file type: {file_path}"
            )