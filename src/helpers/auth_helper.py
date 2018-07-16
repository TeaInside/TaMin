import requests
from src import app
from functools import wraps
from flask import redirect, url_for, flash, json
from flask_login import current_user

CLIENT_ID = app.config.get("GITHUB_CLIENT_ID")
SECRET_ID = app.config.get("GITHUB_SECRET_ID")


def required_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                return redirect(url_for("home.index"))
            return f(*args, **kwargs)

        return wrapped

    return wrapper


def get_access_token(session_code):
    url = "https://github.com/login/oauth/access_token"
    data = {"client_id": CLIENT_ID, "client_secret": SECRET_ID, "code": session_code}
    response = requests.post(url, params=data, headers={"Accept": "application/json"})
    access_token = response.json()
    return access_token["access_token"]


def get_auth_data(access_token):
    url = "https://api.github.com/user"
    data = {"access_token": access_token}
    response = requests.get(url, params=data, headers={"Accept": "application/json"})
    return response.json()
