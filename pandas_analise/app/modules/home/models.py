import pandas as pd

from io import BytesIO
from datetime import datetime

from sqlalchemy import Column, LargeBinary, Integer, String, Date

from ...ext.db import db

class File(db.Model):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key=True)
    file = Column(LargeBinary)
    date = Column(Date, default=datetime.now())
    filename = Column(String)

    def get_table(self):
        data_frame = self.get_data_frame()
        return data_frame.iloc[0:100].values
    
    def get_columns(self):
        return self.get_data_frame().columns

    def get_data_frame(self):
        byte_file = BytesIO(self.file)
        data_frame = pd.read_csv(byte_file, low_memory=False)
        return data_frame
    