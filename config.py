class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # databasetype+driver://user:password@host:port/db_name
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:kozan@localhost:5432/db_name'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_ECHO = True
