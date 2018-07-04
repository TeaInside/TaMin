from src import app
from src import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    messages = db.Column(db.Text())
    