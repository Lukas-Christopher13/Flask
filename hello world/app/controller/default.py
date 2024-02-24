from app import app


@app.route('/')
def homePage():
    return 'My home page'
