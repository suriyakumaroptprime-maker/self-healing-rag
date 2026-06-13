import requests


class APIClient:

    def __init__(self):

        self.base_url = (
            "http://127.0.0.1:8000"
        )

    def upload_file(
        self,
        file_path
    ):

        with open(
            file_path,
            "rb"
        ) as f:

            files = {

                "file": f
            }

            response = (
                requests.post(
                    f"{self.base_url}/upload",
                    files=files
                )
            )

        return response.json()

    def chat(
        self,
        query
    ):

        response = requests.post(

            f"{self.base_url}/chat",

            json={
                "query": query
            }
        )

        return response.json()