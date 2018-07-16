from src import app
from src import db
from datetime import datetime
from src.models.flags import Flag


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messages = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    edited_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"))
    flags = db.relationship("CommentFlag", backref="comment", lazy="dynamic")

    def __repr__(self):
        return "Comment {}".format(self.id)


class CommentFlag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey("comment.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    flag = db.Column(db.Enum(Flag))
