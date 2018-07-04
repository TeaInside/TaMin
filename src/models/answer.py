from src import app
from src import db


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.Text())
    
