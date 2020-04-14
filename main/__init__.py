from flask import Flask
from flask_sqlalchemy import SQLAlchemy



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



from main import routes