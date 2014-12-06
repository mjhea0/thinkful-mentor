from app import app
from flask import Flask, render_template, request, abort

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    error = None
    answer = None
    try :
        a = float(request.form.get("a"))
        b = float(request.form.get("b"))
    except:
        return "Non numerical inputs", 500
        
    op = request.form.get("op")
    if op == '+': answer = a + b
    elif op == '-': answer = a-b
    elif op == '/':
        if b == 0:
            return "Divide by 0", 500
        answer = a / float(b)
    elif op == '*': answer = a*b
    else :
        return "Invalid operator", 500

    return "{}".format(answer)