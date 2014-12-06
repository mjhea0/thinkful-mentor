from app import app, db
from flask import Flask, request, render_template, redirect
from models import Car
from forms import CarDetailsForm, CarFilterForm

@app.route('/')
def index():
    return redirect("/list_cars")

    
@app.route('/list_cars', methods=["GET"])
def get_list_cars():
    cars = Car.query.all()
    form = CarFilterForm()
    return render_template("list_cars.html", cars = cars, form = form)

@app.route('/list_cars', methods=["POST"])
def post_list_cars():
    mfg = request.form.get("mfg")
    if mfg == 'not specified':
        return redirect ('/list_cars')

    cars = Car.query.filter(Car.mfg == mfg).all()
    print "debug", cars
    return render_template("list_cars.html", cars = cars, form=CarFilterForm())



@app.route('/edit_car/<id>', methods=['GET'])
def get_edit_car(id):
    car = Car.query.get(id)
    if car:
        form = CarDetailsForm(obj=car)
        return render_template('car_details.html', form = form)
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
    form = CarDetailsForm()
    return render_template("car_details.html", form=form)

@app.route('/add_car', methods=['POST'])
def post_add_car():
    form = CarDetailsForm()
    if form.validate_on_submit():
        mfg = form.mfg.data
        model = form.model.data
        year = form.year.data
        color = form.color.data
        c = Car(mfg=mfg, model=model, year=year, color=color)
        db.session.add(c)
        db.session.commit()
        return redirect('/list_cars')
    else:
        return render_template("car_details.html", form=form)