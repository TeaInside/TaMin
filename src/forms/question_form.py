from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class QuestionForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    messages = TextAreaField("Question", validators=[DataRequired(), Length(min=50)])
    submit = SubmitField("Submit")

    def validate_messages(self, messages):
        if len(messages.data.strip()) < 50:
            raise ValidationError("Please be specific in your question")
