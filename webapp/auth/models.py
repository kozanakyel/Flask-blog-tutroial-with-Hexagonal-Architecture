from . import bcrypt, AnonymousUserMixin
from .. import db

class User(db.Model):
    #__tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255)) #, nullable=False, index=True, unique=True
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def __init__(self, username=""):
        self.username = username

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password=password)
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password=password)
    
    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False 
        else:
            return True 
        
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False
    
    def get_id(self):
        return str(self.id)
    
    def __repr__(self):
        # formats what is shown in the shell when print is
        # called on it
        return '<User {}>'.format(self.username)
