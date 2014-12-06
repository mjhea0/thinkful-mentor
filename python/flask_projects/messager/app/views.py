from app import app, db
from flask import Flask, request, render_template, redirect
from models import Message

@app.route('/')
def index():
    messages = Message.query.order_by(Message.id.desc()).all()
    return render_template("index.html", messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    txt = request.form.get('message')
    if not txt:
        abort(500)
    m = Message(txt)
    db.session.add(m)
    db.session.commit()
    return redirect('/')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()