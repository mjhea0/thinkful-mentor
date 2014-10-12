from flask import render_template, request, jsonify, session, \
    flash, redirect, url_for
import random
import requests
from functools import wraps

from yummly import app
from yummly import api
from yummly.forms import LoginForm


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if request.form['username'] == "admin" and \
                    request.form['password'] == "admin":
                session['logged_in'] = True
                return redirect(url_for('index'))
            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """
    1. grab ingredient list from form
    2. pass ingredients list to `get_ingredients()`
    3. grab random result
    3. return results to the template
    """
    if request.method == "POST":
        ingredient_list = request.form.get('ingredient_list')
        recipe = []
        try:
            response = api.get_ingredients(ingredient_list)
            recipe = random.choice(response["matches"])
            result = {
                "recipe_id": recipe["id"],
                "recipe_name": recipe["recipeName"],
                "recipe_pic": recipe['imageUrlsBySize']['90'].replace(
                    's90-c', 's230-c'
                )
            }
            code = 200
        except requests.ConnectionError, e:
            result = {"error": e}
            code = 500
        except:
            result = {"error": "Something very bad happened! Please Try again."}
            code = 500
        return jsonify(result), code
    else:
        return render_template("index.html")
