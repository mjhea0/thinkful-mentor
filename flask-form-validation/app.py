from random import randrange
from flask import Flask, render_template
from flask_wtf import Form
from wtforms import TextField, RadioField
from wtforms.validators import Required

# config
SECRET_KEY = 'change-me-please'

app = Flask(__name__)
app.config.from_object(__name__)


# form
class QuestionForm(Form):
    q1 = RadioField(
        'Please answer yes',
        validators=[Required("Please answer the question.")],
        choices=[('yes', 'Yes'), ('no', 'No')])
    q2 = RadioField(
        'Please answer yes',
        validators=[Required("Please answer the question.")],
        choices=[('yes', 'Yes'), ('no', 'No')])
    q3 = RadioField(
        'Please answer yes',
        validators=[Required("Please answer the question.")],
        choices=[('yes', 'Yes'), ('no', 'No')])


# views
def error_list():
    errors = ["first error", "second error", "third error", "fourth error"]
    return errors

def get_form_data(data):
    right_answers = {'q2': u'yes', 'q1': u'yes', 'q3': u'yes'}
    return True if set(data.values()) - set(right_answers.values()) == set([]) else False


@app.route('/', methods=['post', 'get'])
def form():
    form = QuestionForm()
    answer = ""
    errors = ""
    if form.validate_on_submit():
        if get_form_data(form.data) is True:
            answer = "Thanks for submitting!"
        else:
            answer = error_list()[randrange(0, len(error_list()))]
    else:
        errors = form.errors
    return render_template(
        'form.html', form=form, answer=answer, errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
    