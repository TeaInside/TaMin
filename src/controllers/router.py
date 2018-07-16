from src import app
from src.controllers.auth_controller import auth
from src.controllers.home_controller import home
from src.controllers.feedback_controller import feedback
from src.controllers.ask_controller import ask

app.register_blueprint(auth)
app.register_blueprint(home)
app.register_blueprint(feedback)
app.register_blueprint(ask)
