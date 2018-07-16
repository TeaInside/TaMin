from src import app, db
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from src.models.question import Question, QuestionFlag, QuestionVote
from src.models.answer import Answer, AnswerFlag, AnswerVote
from src.models.comment import Comment, CommentFlag
from src.forms.feedback_form import FeedbackForm

feedback = Blueprint("feedback", __name__)


@feedback.route("/feedback/<int:id>", methods=["GET", "POST"])
def view(id):
    question = Question.query.filter_by(id=id).first()
    answers = Answer.query.filter_by(question_id=question.id).all()
    form = FeedbackForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            answer = Answer(messages=form.messages.data)
            answer.user_id = current_user.id
            answer.question_id = question.id
            answer.created_at = datetime.utcnow()
            db.session.add(answer)
            db.session.commit()
            return redirect(url_for("feedback.view", id=question.id))
        return redirect(url_for("auth.login"))
    if request.method == "GET":
        form.messages.data = ""
    return render_template(
        "/feedback/detail.html",
        title="Feedback",
        form=form,
        question=question,
        answers=answers,
    )


@feedback.route("/feedback/solve/<int:id>", methods=["GET"])
def solve(id):
    question = Question.query.get(int(id))
    question.is_solved = True
    db.session.commit()
    return redirect(url_for("feedback.view", id=question.id))
