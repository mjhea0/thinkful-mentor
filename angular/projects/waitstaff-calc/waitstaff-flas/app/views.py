from flask import Flask, render_template, request, jsonify, make_response
from app import app, db
from models import Earning


# routes

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/api/v1/earnings', methods=['GET','POST'])
def sightings():
    if request.method == 'GET':
        # query database
        query = "SELECT * FROM earnings"
        results = Earning.query.from_statement(query).all()
        # set variables
        total_tips = 0
        total_meals = 0
        average_tip = 0
        # calculate total
        for result in results: 
            total_tips += result.tip_rate
            total_meals += 1
        average_tip = total_tips / total_meals
        # create dict
        items = {
            'total_tips': total_tips,
            'total_meals': total_meals,
            'average_tip': average_tip
        }
        return make_response(jsonify(items), 200)
    if request.method == 'POST':
        # handle request
        items = request.json
        price = items['mealPrice']
        tax_rate = items['taxRate']
        tip_rate = items['tipRate']
        # add data to database
        new_entry = Earning(price, tax_rate, tip_rate)
        db.session.add(new_entry)
        db.session.commit()

        return make_response(jsonify({'created':'success'}), 201)

