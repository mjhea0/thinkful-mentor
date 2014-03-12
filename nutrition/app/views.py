
# The views are the handlers that respond to requests from web browsers.
from flask import render_template, flash, request, redirect, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import ProfileForm, RegistrationForm, LoginForm
from models import *
#Base.metadata.create_all(engine)


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Linda' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm(request.form)
    if request.method == 'POST' and form.validate():
        #need to set up salalchemy and reset the redirect to a
        #different url_fo()
        return redirect(url_for('profile'))
    return render_template('profile.html', form=form)

#when user goes to local host:  the function executes.
@app.route('/food_log', methods=['GET','POST'])
def food_log():
    user = db.session.query(User).filter_by(email="happy").first()
    if request.method == 'POST':
        # list comprehension: transforms previous lists iinto a new list n python
        #numbers = [int(x) for x in request.form.getlist('number')]
        #we add multiple foods into the form
        foods = request.form.getlist('food')
        quantities = request.form.getlist('quantity')
        # To get the food log belonging to the existing user, we need to see if it 
        # exists by querying the database/FoodLog Class
        # FoodLog class 

        #this is a single food log
        food_log = db.session.query(FoodLog).filter_by(user=user).first()
        if food_log is None:
            food_log = FoodLog()

            #user attribute of the FoodLog Class is the user currently logged in.
            food_log.user = user
            db.session.add(food_log)

        for food_name, food_quantity in zip(foods, quantities):
            food = db.session.query(Food).filter_by(name=food_name).first()
            if food is None:
                print 'The item %s you enterred is not a proper food. Please try again.' % food_name
                continue
            association = Association()
            #quantity is an attribute of a class
            association.quantity = float(food_quantity)
            #the association will contain one food and one food_log
            association.food = food 
            food_log.foods.append(association)
            #else:
                #to our food_log, we want to get the list of foods and add the desired food to the food_log.
                #food_log.foods.append(food)

        db.session.commit()
        

        
        # add query for finding food in database called Food. 
        # I want to see if the food exists in the database called Food.
        # Give error if food is not in database.
        # Give affirmation for finding food in database.
        # will need to rexamine relationships in models.py
        # refer to sqlalchemy tutorial

        return redirect(url_for('food_log'))


    #we are dealing with one food_log at a time    
    food_log = db.session.query(FoodLog).filter_by(user=user).first()
    print food_log
    if food_log is None:
        food_log = FoodLog()

        #user attribute of the FoodLog Class is the user currently logged in.
        food_log.user = user
        db.session.add(food_log)

    
    # The food_log contains a list of associations between foods and quantities.
    food_nutrient_list = []
    for association in food_log.foods:
        #we are appending to the food_nutrient list a dictionary.
        #The dictionary contains the name of the food and the calculated values of the 
        # nutrients for the certain quantity  for that food.
        food_nutrient_list.append({
            "name": association.food.name, 
            "calorie": association.food.calorie * association.quantity, 
            
            "protein": association.food.protein * association.quantity,
            "carbohydrate": association.food.carbohydrate * association.quantity,
            "fat": association.food.fat * association.quantity
            })
        print association.food, association.quantity
    print food_nutrient_list

    return render_template('food_log.html', food_nutrient_list=food_nutrient_list)
    


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    #form = LoginForm()
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
    #if form.validate_on_submit():

        #flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #need to set up sqlalchemy
        #user = User(form.username.data, form.email.data,
                    #form.password.data)
        #need to set up sqlalchemy
        #db_db.session.add(user)
        #flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

