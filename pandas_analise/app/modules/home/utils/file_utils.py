from io import BytesIO
from typing import List

from ..file import File
from ..dto.file_table_dto import FileTableDTO

class FileUitl:
    def __init__(self, file: File):
        self.byte_file = BytesIO(file.file)

    def get_table(self, lines_number: int) -> FileTableDTO:
        str_lines = self.get_str_lines(lines_number)
        return self.to_table(str_lines)


    def get_str_lines(self, lines: int) -> List[str] :
        str_list: List[str] = list()

        for i in range(lines):
            line = str(self.byte_file.readline(), encoding='utf-8')
            str_list.append(line)
        
        return str_list
        
    def to_table(self, str_list: List[str]) -> FileTableDTO:
        table: List[List[str]] = list()

        for line in str_list:
            splited_line = line.split(",")
            table.append(splited_line)
        
        return FileTableDTO(table)
        