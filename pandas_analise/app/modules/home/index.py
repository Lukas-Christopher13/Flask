from werkzeug.utils import secure_filename
from flask import render_template, request, flash, redirect

from . import home
from .file_repository import FileRepository


file_repository = FileRepository()

@home.route("/", methods=['GET', 'POST'])
def home_index():
    if request.method == "POST":

        if "file" not in request.files :
            flash("No file part")
            return redirect(request.url)
        
        file = request.files["file"]

        if file.filename == "":
            flash("No selected file")
            redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_repository.create(filename, file.stream.read())
            
            return redirect("/")
    
    filenames = file_repository.get_all_filenames()

    return render_template("home/index.html", filenames=filenames)

#tirar essa rota daqui e fazer uma rota file separada com os metodos qu eu quero, assim poderie usar o
#pandas! 
    
def allowed_file(filename):
     return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "csv"