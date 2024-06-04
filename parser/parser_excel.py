import pandas as pd


class ParserExcel:

    def __init__(self, file_path: str):
        self.file = file_path

    def save_file(self, path: str) -> None:
        """Save file."""

    def read_file(self, path: str) -> pd.DataFrame:
        """Read file."""
