from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError


class FeedbackForm(FlaskForm):
    messages = TextAreaField("Feedback", validators=[DataRequired(), Length(min=20)])
    submit = SubmitField("Submit")

    def validate_messages(self, messages):
        if len(messages.data.strip()) < 20:
            raise ValidationError("Please provide good feedback")
