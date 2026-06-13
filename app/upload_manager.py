from pathlib import Path


class UploadManager:

    def __init__(self):

        self.upload_dir = Path(
            "data/uploads"
        )

        self.upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_file(
        self,
        uploaded_file
    ):

        file_path = (
            self.upload_dir
            / uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        return str(file_path)