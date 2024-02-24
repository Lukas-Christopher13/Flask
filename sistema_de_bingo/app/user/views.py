from . import user
from app.models import Cartela
from app import db
from flask import render_template, redirect, url_for, request


@user.route("/cartela/<int:id>")
def cartela(id):
    cartela : Cartela = Cartela.query.filter_by(id=id).first()
    return render_template("user/cartela.html", cartela=cartela)

#funcioalidades
@user.route("/criar_cartelas", methods=["POST"])
def criar_cartelas():
    quantidade = int(request.form['quantidade'])

    for i in range(quantidade):
        db.session.add(Cartela())
    db.session.commit()

    return redirect(url_for("user.index"))


        

    

