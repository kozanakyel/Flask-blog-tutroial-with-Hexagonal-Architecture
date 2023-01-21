from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def page_not_found(error):
    return render_template('404.html'), 404

def create_app(object_name):
    
    app = Flask(__name__)
    app.config.from_object(object_name)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .auth import create_module as auth_create_module
    from .blog import create_module as blog_create_module
    from .main import create_module as main_create_module
    from .api import create_module as api_create_module
    
    auth_create_module(app)
    blog_create_module(app)
    main_create_module(app)
    api_create_module(app)   # for api blogs
    
    return app