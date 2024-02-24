from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/parabens')
def parabens():
	return name

@app.route('/mypost', methods =["GET", "POST"])
def mypost():
	name = request.form.get('name')
	return redirect("/parabens")