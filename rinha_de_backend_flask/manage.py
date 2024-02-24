from app.ext.db import db
from app import create_app

from app.models import *

app = create_app("developmente")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")