import random
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flashcards.db"
app.config["SECRET_KEY"] = "Shhhh!"

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
    rand = random.randrange(0, db.session.query(Question).count()) 
    question = db.session.query(Question)[rand]
    options = generate_options()
    return render_template('home.html',question=question, options=options)

def generate_options():
    # make sure answers don't repeat
    options = []
    while len(options) < 3:
        rand_answer = random.randrange(0, db.session.query(Answer).count())
        answer = db.session.query(Answer)[rand_answer]
        if answer not in options:
            options.append(answer)
    return options

@app.route('/answer/<int:answer_id>')
def answer(answer_id):
    new_id = answer_id
    db.session.query(Answer).filter_by(answer_id = new_id)
    db.session.commit()
    flash('Completed!')
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
