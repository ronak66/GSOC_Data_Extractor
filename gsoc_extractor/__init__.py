from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'

db = SQLAlchemy(app)

from gsoc_extractor import routes
