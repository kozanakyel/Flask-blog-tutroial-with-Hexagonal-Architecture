#source /home/kozan/.pyenv/versions/flask-venv/bin/activate

import os
from dotenv import load_dotenv

load_dotenv() 
SECRET_KEY_ENV = os.getenv('SECRET_KEY')

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = SECRET_KEY_ENV
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
