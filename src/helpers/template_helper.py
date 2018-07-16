from src import app
from src.models.question import Question
from src.models.answer import Answer


def get_trending_question():
    trends = (
        Question.query.filter_by(is_solved=True).order_by(Question.created_at).limit(10)
    )
    return trends


app.jinja_env.globals.update(get_trending_question=get_trending_question)
