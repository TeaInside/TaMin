from src import app, db
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from src.models.question import Question, QuestionFlag, QuestionVote
from src.forms.question_form import QuestionForm

ask = Blueprint("ask", __name__)


@ask.route("/ask", methods=["GET", "POST"])
@login_required
def new():
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(title=form.title.data, messages=form.messages.data)
        question.user_id = current_user.id
        question.created_at = datetime.utcnow()
        db.session.add(question)
        db.session.commit()
        return redirect(url_for("home.index"))
    return render_template("/question/new.html", title="New Question", form=form)


@ask.route("/ask/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    question = Question.query.filter_by(id=id).first()
    form = QuestionForm(obj=question)
    if current_user.id == question.user_id:
        if form.validate_on_submit():
            question.title = form.title.data
            question.messages = form.messages.data
            question.edited_at = datetime.utcnow()
            db.session.commit()
            return redirect(url_for("feedback.view"))
    flash("You're not authorized to edit this question")
    return redirect(url_for("feedback.view"))
