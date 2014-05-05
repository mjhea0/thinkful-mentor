from flask_wtf import Form
from wtforms import SubmitField, RadioField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, ValidationError
from random import randrange


class CorrectAnswer(object):
    """
    Custom validator for WTForms to check
    if the correct answer was submitted
    """

    def __init__(self, answer):
        self.answer = answer

    def __call__(self, form, field):
        # List of error messages that are selected by random
        error_messages = ['Sorry, that\'s not the correct answer.',
                          'Try that again...',
                          'Incorrect answer.',
                          'Please check this answer...',
                          'Oops! Try again...',
                          'Nope! Sorry... try again!',
                          'No, not quite... try again!',
                          'Hmmm, not exactly right...']
        num = randrange(0, len(error_messages))
        message = error_messages[num]

        if field.data != self.answer:
            raise ValidationError(message)


class PopQuiz(Form):
    q1 = RadioField(
        "1. The answer to question one is False.",
        choices=[('True', 'True'), ('False', 'False')],
        validators=[CorrectAnswer('False')]
        )

    q2 = RadioField(
        "2. The answer to this question is True.",
        choices=[('True', 'True'), ('False', 'False')],
        validators=[CorrectAnswer('True')]
        )

    q3 = SelectMultipleField(
        "3. The correct answer is 1, 2 and 3.",
        choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four')],
        validators=[CorrectAnswer(['1', '2', '3'])],

        # changes the choices into checkboxes instead of a dropdown list
        option_widget=widgets.CheckboxInput(),

        # puts the checkboxes in front of the label
        widget=widgets.ListWidget(prefix_label=False)
        )

    q4 = SelectMultipleField(
        "4. Select 'None Of The Above'",
        choices=[
            ('1', 'None'),
            ('2', 'Some'),
            ('3', 'A few'),
            ('4', 'I\'m not sure...'),
            ('5', 'None of the above!')
        ],
        validators=[CorrectAnswer(['5'])],

        # changes the choices into checkboxes instead of a dropdown list
        option_widget=widgets.CheckboxInput(),

        # puts the checkboxes in front of the label
        widget=widgets.ListWidget(prefix_label=False))

    submit = SubmitField("Submit")
