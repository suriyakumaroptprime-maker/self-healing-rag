import easyocr


class ImageLoader:

    def __init__(self):

        self.reader = easyocr.Reader(
            ['en'],
            gpu=False
        )

    def load(
        self,
        image_path: str
    ) -> str:

        results = self.reader.readtext(
            image_path
        )

        extracted_text = []

        for result in results:

            text = result[1]

            extracted_text.append(
                text
            )

        return "\n".join(
            extracted_text
        )