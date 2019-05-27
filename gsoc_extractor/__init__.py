from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

from gsoc_extractor import routes
