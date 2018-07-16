from src import app, db
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, login_user, logout_user
from src.models.user import User, UserType
from src.helpers.auth_helper import required_roles, get_access_token, get_auth_data


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login():
    if not current_user.is_anonymous:
        return redirect(url_for("home.index"))
    client_id = app.config.get("GITHUB_CLIENT_ID")
    url = "https://github.com/login/oauth/authorize?scope=read:user&client_id={}".format(
        client_id
    )
    return redirect(url)


@auth.route("/auth", methods=["GET"])
def github_auth():
    session_code = request.args["code"]
    access_token = get_access_token(session_code)
    auth_data = get_auth_data(access_token)
    if auth_data["login"] is None:
        flash("Authentication failed")
        return redirect(url_for("home.index"))
    user = User.query.filter_by(username=auth_data["login"]).first()
    if not user:
        user = User(username=auth_data["login"], email=auth_data["email"])
        user.account_type = UserType.USER
        user.avatar_url = auth_data["avatar_url"]
        user.html_url = auth_data["html_url"]
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    flash("Authentication succesful")
    return redirect(url_for("home.index"))


@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("home.index"))
