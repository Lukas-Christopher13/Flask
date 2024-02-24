from flask import g, Flask

app = Flask(__name__)

@app.route("/")
def teste():
    g.db = "Funciona!"
    g.teste = "teste"
    if "db" in g:
        return "estava"
        
    return "não estava"

@app.route("/test")
def novaRota():
    if 'db' not in g:
        g.db = "coloquei algo!"
    

    return g.db