from models import *

db.create_all()

# creating a user instance.  Passing in the arguments as defined in models.py;
# name, password, email, calorie_goal, protein_goal, carbohydrate_goal, fat_goal, weight.
linda_user = User('Linda', 'hello', 'Linda.C.Palay@gmail.com')

# session is a holding/staging area before committing.
db.session.add(linda_user)


# now the object is being added to the database


# create a food instance. name, calories, protein, carbs, fat.
blackbeans = Food("blackbeans", 100, 9, 24, 1)
spinach_cooked = Food("spinach_cooked", 100, 23, 3, 0)
brazil_nuts = Food("brazil_nuts", 65.6, 1.43, 1.23, 6.64)
session.add(blackbeans)
session.add(spinach_cooked)
session.add(brazil_nuts)
session.commit()

# helper function for getting user_id.
def grab_user_id(name):
    results = session.query(User).filter(User.name == name).all()#can pass in any name
    for result in results:
        return result.id

# assigning user_id to a variable.
user_id = grab_user_id("Linda")

# creating a food_log instance. witih the food_name, food_quantity, user_id.
linda_food_log = FoodLog('blackbeans', 80)
print linda_food_log

# I need to set up a relationship between food_log and food







