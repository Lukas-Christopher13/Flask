import pytest
import pandas as pd
import numpy as np

from    app.modules.home.models import File
from    app.modules.home.file_controller import FileController
from    app.modules.home.file_repository import FileRepository

repository = FileRepository()


def test_aprendendo():

    df = pd.read_csv("arquivos_csv_test/passwords.csv")
    file = repository(1)
    df.head()
    
    assert True


