from app import db

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
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return self.description