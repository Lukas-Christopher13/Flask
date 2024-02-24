from flask import Flask
from flask import render_template, redirect
from flask_bootstrap import Bootstrap
from my_form import MyForm
from data_base import db
from model import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:lukas@localhost:5432/flask_data_base"

db.init_app(app)

bootstrap =  Bootstrap(app)

with app.app_context():
    db.create_all()

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
