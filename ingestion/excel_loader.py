import pandas as pd


class ExcelLoader:

    def load(
        self,
        file_path: str
    ) -> str:

        excel_file = pd.ExcelFile(
            file_path
        )

        text = ""

        for sheet_name in (
            excel_file.sheet_names
        ):

            df = pd.read_excel(
                file_path,
                sheet_name=sheet_name
            )

            text += (
                f"\n\n=== SHEET: "
                f"{sheet_name} ===\n\n"
            )

            text += (
                df.to_string(
                    index=False
                )
            )

        return text