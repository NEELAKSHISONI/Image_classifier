from flask import Flask
from .models import db, User

from models import db, User  # Assuming models are defined in a file named models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_management/db.sqlite'
db.init_app(app)

with app.app_context():
    db.create_all()
