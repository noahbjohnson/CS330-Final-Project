from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User
from flask_login import current_user
from datetime import datetime, timedelta


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=12, max=64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=64)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('The desired username is already in use.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Account already created for this email, please login.')
        if email.data[-11:] != "@luther.edu":
            raise ValidationError('Sign-up requires a luther.edu email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    enable_last_seen = BooleanField('Show last seen time on your profile')
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None and user.username != current_user.username:
            raise ValidationError('The desired username is already in use.')
        elif abs(datetime.utcnow() - current_user.username_last_changed) < timedelta(days=7) and username.data != current_user.username:
            raise ValidationError('You cannot change your username more than once in a week. Please wait: {}'
                                  .format(str((current_user.username_last_changed+timedelta(days=7))-datetime.utcnow())))

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=5, max=1400)])
    submit = SubmitField('Submit')
