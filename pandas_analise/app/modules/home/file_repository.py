from .models import File

from ...ext.db import db

class FileRepository:
    def create(self, filename, file):
        file = File(filename=filename, file=file)

        db.session.add(file)
        db.session.commit()

    def get(self, id):
        file = db.session.query(File).filter(File.id == id).first()
        return file

    def get_all_filenames(self):
        filenames = db.session.query(File.id, File.filename, File.date).all()
        return filenames
    

        