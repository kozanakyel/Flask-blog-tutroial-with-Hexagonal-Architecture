#source /home/kozan/.pyenv/versions/flask-venv/bin/activate

class Config(object):
    POSTS_PER_PAGE = 10

class ProdConfig(Config):
    SECRET_KEY = '\x99\xe4(\xd9+\xcc\xd8Ut\x9bL^v\xb5\xc8\xea\x1c\x05j\x8cWj\xd6C'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '\xa8P>~O\x10\xce\xdev\xf0E\xfd\xa2E (W\x8d\xa4\xc9\x80A\xca\xcd'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
