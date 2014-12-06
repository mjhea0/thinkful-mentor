from app import app, db
from flask import Flask, request, render_template, redirect
from models import Car

@app.route('/')
def index():
    return redirect("/list_cars")
    
@app.route('/list_cars', methods=["GET"])
def get_list_cars():
    cars = Car.query.all()
    print "debug", cars
    return render_template("list_cars.html", cars = cars)

@app.route('/list_cars', methods=["POST"])
def post_list_cars():
    mfg = request.form.get("mfg")
    if mfg == 'not specified':
        return redirect ('/list_cars')

    cars = Car.query.filter(Car.mfg == mfg).all()
    print "debug", cars
    return render_template("list_cars.html", cars = cars)



@app.route('/edit_car/<id>', methods=['GET'])
def get_edit_car(id):
    car = Car.query.get(id)
    if car:
        return render_template('edit_car.html', car=car)
    else:
        abort(404)

@app.route('/edit_car/<id>', methods=['POST'])
def post_edit_car(id):
    car = Car.query.get(id)
    if not car:
        abort(404)

    car.make = request.form.get("make")
    car.model = request.form.get("model")
    car.year = request.form.get("year")
    car.color = request.form.get("color")
    db.session.commit();

    return redirect("/list_cars")

@app.route('/delete_car/<id>', methods=['GET'])
def delete_car(id):
    car = Car.query.get(id)
    if car:
        db.session.delete(car)
        db.session.commit()
        return redirect("/list_cars")
    else:
        abort(404)

@app.route('/add_car', methods=['GET'])
def get_add_car():
    return render_template("add_car.html")

@app.route('/add_car', methods=['POST'])
def post_add_car():
    mfg = request.form.get("mfg")
    model = request.form.get("model")
    year = request.form.get("year")
    year = year if year else 0
    color = request.form.get("color")

    c = Car(mfg=mfg, model=model, year=year, color=color)
    db.session.add(c)
    db.session.commit()
    return redirect('/list_cars')
