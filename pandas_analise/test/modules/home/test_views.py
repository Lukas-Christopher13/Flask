import pytest

from app.modules.home.index import allowed_file

def test_allowed_file_csv_file():
    assert allowed_file("datas.csv") == True

def test_alowed_file_invalid_file():
    assert allowed_file("datas.html") == False