from flask import Flask, render_template, request
from app import app

app.debug = True

@app.route('/')
def index() :
    return render_template("index.html")

@app.route('/answer', methods=["POST"])
def answer():
    
    try :
        a = float(request.form.get("a"))
        b = float(request.form.get("b"))
    except:
        return render_template("answer.html", answer="", 
            error="Error, non-numerical input.")
    
    answer = None
    op = request.form.get("op")
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a-b
    elif op == r'/':
        if b == 0:
            return render_template("answer.html", answer="", 
        error="Error, divide by 0.")
        answer = a/float(b)
    elif op == '*':
        answer = a*b
    else :
        return render_template("answer.html", answer=answer, 
        error="Error, invalid operator")
        

    return render_template("answer.html", answer=answer, error="")