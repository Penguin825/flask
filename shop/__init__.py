from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '76cc7027fa79aae3ed9b6153489c49958410b5c8496a7419'
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

from shop import routes
