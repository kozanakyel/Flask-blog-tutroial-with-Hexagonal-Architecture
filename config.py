#source /home/kozan/.pyenv/versions/flask-venv/bin/activate

class Config(object):
    POSTS_PER_PAGE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    # databasetype+driver://user:password@host:port/db_name
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/flask_test_db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_ECHO = True
