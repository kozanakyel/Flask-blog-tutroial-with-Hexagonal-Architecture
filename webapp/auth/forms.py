from wtforms import (
    StringField,
    TextAreaField,
    PasswordField,
    BooleanField
)
from .models import User
from flask_wtf import FlaskForm as Form
from wtforms.validators import DataRequired, Length, EqualTo, URL

class LoginForm(Form):
    username = StringField('Username', [DataRequired()], Length(max=255))
    password = PasswordField('Password', [DataRequired()])
    
    def validate(self):
        check_validate = super(LoginForm, self).validate()
        if not check_validate:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True