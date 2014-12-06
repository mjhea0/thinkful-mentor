from app import app, db, lm, oid
from flask import Flask, request, render_template, redirect, g
import models
from flask.ext.login import url_for, login_user, logout_user, current_user, login_required
import forms
import config

@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    form = forms.LoginForm()

    if g.user:
        if not g.user.is_anonymous():
            return redirect("/list_cars")

    if request.method == 'POST':
        oid_url = config.OPENID_PROVIDERS[form.oid_provider.data]
        return oid.try_login(oid_url, 
            ask_for = ['nickname', 'email'])

    return render_template('login.html', 
        title = 'Sign In',
        form = form)

    
    
@oid.after_login
def after_login(resp):
    if not resp.email:
        abort(404)

    user = models.User.query.filter(models.User.email == resp.email).first()
    
    if not user:
        user = models.User(resp.email)
        db.session.add(user)
        db.session.commit()

    login_user(user)
    
    return redirect(url_for('get_list_cars'))



@app.route('/list_cars', methods=["GET"])
@login_required
def get_list_cars():
    cars = g.user.cars
    return render_template("list_cars.html", cars = cars, user=g.user)

@app.route('/list_cars', methods=["POST"])
@login_required
def post_list_cars():
    mfg = request.form.get("mfg")
    if mfg == 'not specified':
        return redirect (url_for('get_list_cars'))

    cars = g.user.cars.filter(models.Car.mfg == mfg).all()
    return render_template("list_cars.html", cars = cars, user=g.user)

@app.route('/edit_car/<id>', methods=['GET'])
@login_required
def get_edit_car(id):
    car = models.Car.query.get(id)
    if car and car.owner == g.user:
        return render_template('edit_car.html', car=car, user=g.user)
    else:
        abort(404)

@app.route('/edit_car/<id>', methods=['POST'])
@login_required
def post_edit_car(id):
    car = models.Car.query.get(id)
    if car and car.owner == g.user:
        car.make = request.form.get("make")
        car.model = request.form.get("model")
        car.year = request.form.get("year")
        car.color = request.form.get("color")
        db.session.commit();

        return redirect(url_for("get_list_cars"))
    else:
        abort(404)
    
@app.route('/delete_car/<id>', methods=['GET'])
@login_required
def delete_car(id):
    car = models.Car.query.get(id)
    if car and car.owner == g.user:
        db.session.delete(car)
        db.session.commit()
        return redirect(url_for("get_list_cars"))
    else:
        abort(404)

@app.route('/add_car', methods=['GET'])
@login_required
def get_add_car():
    return render_template("add_car.html", user=g.user)

@app.route('/add_car', methods=['POST'])
@login_required
def post_add_car():
    mfg = request.form.get("mfg")
    model = request.form.get("model")
    year = request.form.get("year")
    year = year if year else 0
    color = request.form.get("color")

    c = models.Car(mfg=mfg, model=model, year=year, color=color)
    g.user.cars.append(c)
    db.session.commit()
    return redirect(url_for("get_list_cars"))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))