import random
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flashcards.db"
app.config["SECRET_KEY"] = "Shhhh!"

db = SQLAlchemy(app)

class Question(db.Model):

    __tablename__ = "questions"

    question_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return self.description

class Answer(db.Model):

    __tablename__ = "answers"

    answer_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    question_id = db.Column(db.Integer, ForeignKey('questions.question_id'))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return self.description

@app.route('/', methods=['GET'])
def home():
    question = grab_question()
    options = generate_options(question)
    return render_template('home.html',question=question, options=options)

def grab_question():
    rand = random.randrange(0, db.session.query(Question).count()) 
    question = db.session.query(Question)[rand]
    return question

def generate_options(question):
    options = []
    # grab option associated with the question
    option = db.session.query(Answer).filter(Answer.question_id == question.question_id).first()
    options.append(option)
    while len(options) < 3:
        rand_answer = random.randrange(0, db.session.query(Answer).count())
        answer = db.session.query(Answer)[rand_answer]
        if answer not in options:
            options.append(answer)
    return options

def correct_answer(question,options):
    pass

@app.route('/answer/<int:answer_id>')
def answer(answer_id):
    new_id = answer_id
    db.session.commit()
    flash('Completed!')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
