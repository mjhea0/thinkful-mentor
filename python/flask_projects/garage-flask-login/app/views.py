from app import app, db, lm
from flask import Flask, request, render_template, redirect, g
from models import Car, User
from flask.ext.login import url_for, login_user, logout_user, current_user, login_required

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def index():
    return redirect("/login")

@app.route('/login', methods=["GET"])
def get_login():
    if g.user:
        if not g.user.is_anonymous():
            return redirect("/list_cars")
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def post_login():
    remember_me = request.form.get("remember_me")
    email = request.form.get("email")
    user = User.query.filter(User.email == email).first()
    if user:
        login_user(user, remember = remember_me)
        return redirect("/list_cars")
    else:
        return render_template("login.html", error="Invalid login")


@app.route('/list_cars', methods=["GET"])
@login_required
def get_list_cars():
    cars = g.user.cars
    print "debug", cars
    return render_template("list_cars.html", cars = cars, user=g.user)

@app.route('/list_cars', methods=["POST"])
@login_required
def post_list_cars():
    mfg = request.form.get("mfg")
    if mfg == 'not specified':
        return redirect ('/list_cars')

    cars = g.user.cars.filter(Car.mfg == mfg).all()
    print "debug", cars
    return render_template("list_cars.html", cars = cars, user=g.user)

@app.route('/edit_car/<id>', methods=['GET'])
@login_required
def get_edit_car(id):
    car = Car.query.get(id)
    if car and car.owner == g.user:
        return render_template('edit_car.html', car=car, user=g.user)
    else:
        abort(404)

@app.route('/edit_car/<id>', methods=['POST'])
@login_required
def post_edit_car(id):
    car = Car.query.get(id)
    if car and car.owner == g.user:
        car.make = request.form.get("make")
        car.model = request.form.get("model")
        car.year = request.form.get("year")
        car.color = request.form.get("color")
        db.session.commit();

        return redirect("/list_cars")
    else:
        abort(404)
    
@app.route('/delete_car/<id>', methods=['GET'])
@login_required
def delete_car(id):
    car = Car.query.get(id)
    if car and car.owner == g.user:
        db.session.delete(car)
        db.session.commit()
        return redirect("/list_cars")
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

    c = Car(mfg=mfg, model=model, year=year, color=color)
    g.user.cars.append(c)
    db.session.commit()
    return redirect('/list_cars')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))