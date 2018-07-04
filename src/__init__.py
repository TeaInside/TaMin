from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from flask_login import LoginManager
from config.application import DevelopmentConfig

app = Flask(__name__, static_folder="assets", template_folder="views")
app.config.from_object(DevelopmentConfig)
moment = Moment(app)
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
