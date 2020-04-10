from flask import Flask, render_template, url_for, flash, redirect
from forms import signupform, signinform
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

#imported all things


app = Flask(__name__)

app.config['SECRET_KEY'] = '356c2f03e9fd4d3c4287a1366c97fa24'
#csrf thing
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcBHOQUAAAAADf4u1nvZ7aAaR3a8G_9_u7oobAB'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcBHOQUAAAAAKUgkjvxe0qUedGHotX8aP6MagvZ'
#recaptcha things
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#gives location of the database file, or basically creates a database file when we do create all.
db = SQLAlchemy(app)
#SQLAlchemy thigns





class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(120), unique=True, nullable=False)

    email = db.Column(db.String(20), unique=True, nullable=False)

    birthdate = db.Column(db.String(120), unique=False, nullable=False)

    selects = db.Column(db.String(120), unique=False, nullable=False)

    radios = db.Column(db.String(120), unique=False, nullable=False)

    password = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

#Basically a database thing
#id gives a id, and primary key set to true provides a key even if not input.
#username is sth we will use in the database obviously and also i have to learn how to connect to classes inside a database from the Corey Schafer videos.
#others are similar
#the classes inside are important
#primary_key gives key
#unique should be unique
#nullable cant be left empty
#default gives provided value in case data not given


#thre __repr__(self):
#this thing is required to give out the values mentioned in it, whatever is called is then used in the datbase

#in cmdline
#python in project dir
#from main import db
#db.create_all()




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


if __name__ == '__main__':
    app.run(debug=True)
