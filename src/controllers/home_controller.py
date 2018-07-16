from src import app, db
from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import current_user, login_required, login_user, logout_user
from src.helpers.auth_helper import required_roles
from src.models.question import Question

home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
@home.route("/index", methods=["GET"])
def index():
    questions = Question.query.order_by(Question.created_at.desc())
    return render_template("/application/home.html", title="Home", questions=questions)
