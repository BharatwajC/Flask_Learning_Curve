from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # giving it a random name here it is market.db
#we will point it to where we are going to store our database file
#we are configuring our flask application app. key value convention
#URI - Uniform Resource Identifier - just to identify a file as a database

app.config["SECRET_KEY"] = "d2144882cbde0e45f0157396"#This should be enough to show our terminal


db = SQLAlchemy(app) #database instance and passing application as an argument

bcrypt = Bcrypt(app)    #For hashed password creating an instance if bcrypt

login_manager = LoginManager(app)

login_manager.login_view = "login_page"      #To redirect the login_required page to login page
login_manager.login_message_category = "info"        #automaticaaly gives a flash message, here we are just adding a category for better visual


from market import routes       # for the recognition of the routes

