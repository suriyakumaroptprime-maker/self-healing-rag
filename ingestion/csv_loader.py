import pandas as pd


class CSVLoader:

    def load(
        self,
        file_path: str
    ) -> str:

        df = pd.read_csv(
            file_path
        )

        return df.to_string(
            index=False
        )