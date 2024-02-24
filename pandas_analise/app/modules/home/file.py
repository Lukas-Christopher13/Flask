from flask import render_template

from io import BytesIO

from . import home
from .models import File
from .utils.file_utils import FileUitl
from .file_repository import FileRepository

PAGE_LINES = 100


file_repository = FileRepository()


@home.route("/file/<file_id>")
def file(file_id):
    file = file_repository.get(file_id)

    return render_template("/home/file.html", file=file)