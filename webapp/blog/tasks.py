import datetime
from flask import current_app
from flask import render_template

from .. import celery
from .models import Post

#celery -A celery_runner worker --loglevel=info

@celery.task()
def log(msg):
    return msg


@celery.task()
def multiply(x, y):
    return x * y