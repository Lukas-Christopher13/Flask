from app.ext.data_base import db
from app.models import Cartela

from app import create_app

app = create_app("developmnet")

with app.app_context():
    db.create_all()

@app.shell_context_processor
def shell_context():
    return {"db": db, "Cartela":Cartela}

if __name__ == "__main__":
    app.run(debug=True)

