from src import app, db


@app.shell_context_processor
def make_shell_context():
    return {"app": app, "db": db}
