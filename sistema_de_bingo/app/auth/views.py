from . import auth 

from flask import render_template

#to do
@auth.route("/register", methods=["GET", "POST"])
def register():
    return render_template("/auth/register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("/auth/login.html")