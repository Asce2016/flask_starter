from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'Sup3r$3cretkey'

UPLOAD_FOLDER = './app/static/uploads'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://lab5:calabar12@localhost/lab5"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
app.config.from_object(__name__)
from app import views