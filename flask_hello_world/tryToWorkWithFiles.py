from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def myHtmlFile():
	return render_template("teste.html")

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)