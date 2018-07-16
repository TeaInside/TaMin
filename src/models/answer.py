from src import app
from src import db
from datetime import datetime
from src.models.comment import Comment
from src.models.flags import Flag


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    edited_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    comments = db.relationship("Comment", backref="answer", lazy="dynamic")
    flags = db.relationship("AnswerFlag", backref="answer", lazy="dynamic")
    votes = db.relationship("AnswerVote", backref="answer", lazy="dynamic")

    def __repr__(self):
        return "Answer {}".format(self.id)


class AnswerFlag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    flag = db.Column(db.Enum(Flag))


class AnswerVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
