import pytest
import pandas as pd

from app.ext.db import db
from app.modules.home.models import File


def test_get_file(app):
    df = pd.read_csv("arquivos_csv_test/passwords.csv")

    strl = df.iloc[0:5]

    assert True
