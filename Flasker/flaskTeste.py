from flask import Flask, render_template, request, redirect

app = Flask(__name__)

studants = []

@app.route("/")
def index():
	name = request.args.get("name")
	if not name:
		name = "foi"
	return render_template("index.html", name=name)

@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name")
	dorm = request.form.get("dorm")

	if not name or not dorm:
		return render_template("not.html")
	
	studants.append(f"{name} lives in {dorm}")

	return redirect("/registers")

@app.route("/registers")
def registers():
	return render_template("registers.html", studants=studants)