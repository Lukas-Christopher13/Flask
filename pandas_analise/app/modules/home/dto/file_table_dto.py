from typing import List

from ..models import File

class FileTableDTO:
    def __init__(self, file: File) -> None:
        self.data_frame = file.get_data_frame()
        self.head: List[str] = file.get_columns()

    def get_column(self, column: str):
        pass
        


