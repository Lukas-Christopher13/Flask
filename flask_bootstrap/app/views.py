from flask import Blueprint, render_template, redirect
from .forms.produto import ProdutosForm
from .repository.produtos_repository import ProdutosRepository

home_page = Blueprint("home_page", __name__)

repo = ProdutosRepository()

@home_page.route("/")
def index():
    produtos = repo.select()
    return render_template("index.html", produtos=produtos)

@home_page.route("/add", methods=["GET", "POST"])
def add_product():
    form = ProdutosForm()
    if form.validate_on_submit():
        name = form.name.data
        quantidade = form.quantidade.data
        forncecedor = form.fornecedor.data
        
        repo.insert(name, quantidade, forncecedor)

        return redirect("/")
    return render_template("add.html", form=form)

@home_page.route("/test")
def test():
    return render_template("test.html")
