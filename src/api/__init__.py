'''
CS 3700 - Networking & Distributed Computing - Fall 2024
Instructor: Thyago Mota
Student:
Description: Activity 13 - Quotes API
'''

from flask import Flask

app = Flask("Quotes API")

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
db.init_app(app)

# db from models
# from app import models
# with app.app_context():
#     db.create_all()

from api import routes