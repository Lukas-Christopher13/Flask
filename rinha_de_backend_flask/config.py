class Config:
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:lukas@postgres/flask_rinha"

class TestConfig(Config):
    #SQLALCHEMY_DATABASE_URI = "postgresql://postgres:lukas@localhost:5432/test_rinha_flask"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:lukas@postgres/flask_rinha"

config = {
    "test": TestConfig,
    "developmente": DevelopmentConfig
}