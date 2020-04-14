
from flask import  render_template, url_for, flash, redirect
from main import app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from main.forms import signinform, signupform
from main.models import User
from main import db



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title_given="Home")


@app.route("/about")
def about():
    return render_template("about.html", title_given="About")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = signupform()
    if form.validate_on_submit():
        






        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, birthdate = form.birthdate.data, selects = form.selects.data, radios = form.radios.data)
        db.session.add(new_user)
        db.session.commit()
        #so what i did here was the basic db things that i was doing in cmd line
        #i just reated a new instance of User class called new_user
        #everything i put into signup form was the passed into different attributes of the db User class and then was added and committed
        #this put in our signup data
        #also hashed the password before puting into database using generate has from werzeug security with method as sha256 that converts password to 80 characters long



        flash('New user created', 'success')
        

    return render_template("signup.html", title_given="SignUp", form=form)


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    form = signinform()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        #assigned the email value from user filtered by email from which email was equal to form input as user and picked up the first entry 

        if user:
            #if the email exists
            if check_password_hash(user.password, form.password.data):
                #if the hashed password already saved in databse matches with the password from form that is hashed by this method and checked.
                flash('Sign In Successfu', 'success')
                #flash
            else:
                flash ('Invalid Email Address or Password', 'danger')
        
        else:
            flash ('Invalid Email Address or Password', 'danger')

    
                
        

    return render_template("signin.html", title_given="SignIn", form=form)

    
