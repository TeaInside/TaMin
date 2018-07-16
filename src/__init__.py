import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_login import LoginManager

app = Flask(__name__, static_folder="assets", template_folder="views")
app.config.from_object(os.environ.get("APP_CONFIG"))
moment = Moment(app)
login = LoginManager(app)
login.login_view = "auth.login"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from src.controllers import router
from scripts.user import user_command
from src.helpers.template_helper import get_trending_question
