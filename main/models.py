
from main import db



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

