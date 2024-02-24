class Config:
    SECRET_KEY = "change this"
    UPLOAD_FOLDER = "app/files"

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI =  "sqlite:///:memory:"

config = {
    "develpmente" : DevelopmentConfig,
    "testing": TestingConfig
}