from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User



class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20),])

    email=StringField('Email',validators=[DataRequired(),Email()])

    password=PasswordField('Password',validators=[DataRequired(),Length(min=5,max=15)])

    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a differen one.')       

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])

    password=PasswordField('Password',validators=[DataRequired(),Length(min=5,max=15)])
    remember=BooleanField('Remember Me')

    submit=SubmitField('Login In')


class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])

    email=StringField('Email',validators=[DataRequired(),Email()])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','jpeg','png'])])

    submit=SubmitField('Update')

    def validate_username(self,username):
        if(username.data!=current_user.username):
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    def validate_email(self,email):
        if(email.data!=current_user.email):
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a differen one.')       

class RequestResetForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])

    submit=SubmitField('Request Password Reset')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email.You must register first')

class ResetPasswordForm(FlaskForm):
    password=PasswordField('Password',validators=[DataRequired(),Length(min=5,max=15)])

    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Reset Password')