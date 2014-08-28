# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Define WSGI object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Home page view
@app.route('/')
def home():
    return render_template('home.html')


from app.mod_1 import views 


# Build the database:
# This will init the db
db.init_app(app)
