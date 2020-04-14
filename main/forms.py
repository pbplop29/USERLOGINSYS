from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, Form, RadioField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField
from main.models import User

#so obviously imported Flaskform
#imported RecaptchaField from flask_wtf because it is somewhat different from ususal wtforms fields
#imported fields
#imported validators
#imported the Datefield from html5, this shows the drop down thing 


class signupform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    #StringField --> just a field for regular string
    # DataRequired() --> cant leave the field empty
    #Length(min=x, max=y) --> Data cannot be less than x and greater than y


    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    #Email() --> checks if the input is correct email format

    birthdate = DateField("Date of Birth", format='%Y-%m-%d', validators=[DataRequired()])

    #DateField -> for the date drop down and we set this sepecific format because the date no matter the format we use in the UI gets rendered in this format

    password = PasswordField('Password', validators=[DataRequired()])

    #PasswordField --> Bulletifies the characters

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    #EqualTo() --> checks if the provided field is equal to the field mentioned withis this

    recaptcha = RecaptchaField()

    #RecaptchaField() --> just enables the recaptcha thing at this place, recaptcha is a little different as it requires keys to be put in the main file, the keys we recieve from the recaptcha providing host.
                # I used GOOGLE recaptcha services

    

    radios = RadioField('Gender', default='3', choices= [('1', 'Male'), ('2', 'Female'), ('3', 'Confidential')])

    #RadioField --> basiaacally the choose from options
            #--> in our form helpers we have used these such that the first value in choices is the id and second is the label

    selects = SelectField("age group", choices=[
        ('1', '0-10'), ('2', '10-25'), ('3', '35-60'), ('4', '50+')
    ])

    #basically a drop down seclection
    #acts as a pop up radio field thing but works with the form helper of regular things
    submit = SubmitField('Sign Up')
    
    #Genertaes a submit button which acts as post

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username already exists.')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email already exists.')
    # Information about these functions are in       this link:
        # imgur.com/a/3582lY4





class signinform(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    #A True or flase thing

    submit = SubmitField('Sign In')
