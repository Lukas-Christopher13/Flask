class Config:
    SECRET_KEY = "Uma chave muito secreta"
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:lukas@localhost:5432/bingo_database"

class TestConfig(Config):
    pass

config = {
    "developmnet": DevelopmentConfig,
    "test": TestConfig
}