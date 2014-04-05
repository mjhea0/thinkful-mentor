import random
import os
from flask import Flask, render_template, request, session, g, redirect, \
    abort, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import *

# routes
@app.route('/', methods=['GET'])
def home():
    question = get_question()
    options = get_options(question)
    return render_template('home.html',question=question, options=options)

@app.route('/answer/<int:answer_id>/<string:question>')
def answer(answer_id, question):
    updated_question = (str(question))
    answer_query    = db.session.query(Answer).filter(Answer.answer_id == str(answer_id)).first()
    question_query  = db.session.query(Question).filter(Question.description == updated_question).first()
    right_answer    = db.session.query(Question).filter(Question.description == updated_question).first()
    answer = get_correct_answer(right_answer)
    if answer_query.question_id == question_query.question_id:
        correct = flash("Correct!")
        return render_template('check.html', correct=correct)
    else:
        incorrect = flash(('Wrong. The correct answer is "{}"').format(answer))
        return render_template('check.html', incorrect=incorrect)

# helper functions
def get_question():
    rand = random.randrange(0, db.session.query(Question).count()) 
    question = db.session.query(Question)[rand]
    return question

def get_options(question):
    """
    1. pass in the question
    2. get the answer associated with that question
    3. append that answer to the list
    4. grab two more random answers, append them to the list
    """
    options = []
    option = get_correct_answer(question)
    options.append(option)
    while len(options) < 3:
        rand_answer = random.randrange(0, db.session.query(Answer).count())
        answer = db.session.query(Answer)[rand_answer]
        if answer not in options:
            options.append(answer)
    shuffled = random.sample(options, len(options))
    return shuffled

def get_correct_answer(question):
    answer = db.session.query(Answer).filter(Answer.question_id == question.question_id).first()
    return answer


if __name__ == "__main__":
    app.run(debug=True)