import random

questions = {
    "strong": "Do ye want yer drink strong?",
    "salty": "Do ye want it with a salty tang?",
    "bitter": "Are ye a lubber who wants it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["shot of tequila", "glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["seaweed flakes","olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["minced radicchio","shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["powdered lead", "sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["durian puree", "slice of orange", "dash of cassis", "cherry on top"]
}

stockUsed = {}

for style in ingredients:
    for ingredient in ingredients[style]:
        stockUsed[ingredient] = random.randint(1, 6)

adjectives = ["Furry", "Balding", "Slutty", "Shiny", "Uncultured"]
nouns = ["Dingo", "Jackhammer", "Navel", "Superhero", "Doughnut"]

customers = {}


def get_drink_style(drink_style_dict):

    for style in questions.keys():
        response = raw_input(questions[style] + " ")
        drink_style_dict[style] = response.lower() in ("y", "yes")

    return drink_style_dict


def construct_drink(drink_style_dict):

    drink = []

    for style in drink_style_dict.keys():

        if drink_style_dict[style] is True:

            randomChoice = random.choice(ingredients[style])

            if stockUsed[randomChoice] == 0:
                print "\n Arrr... be right back, need to refill my", randomChoice, "supply."
                stockUsed[randomChoice] == random.randint(1, 5)
            else:
                stockUsed[randomChoice] -= 1

            drink.append(randomChoice)
            if randomChoice in stockUsed:
                stockUsed

    return drink


def serve_customer(customer_name):

    while True:

        if customers[customer_name]["numDrunk"] > 4:
            print "\nYar too drunk to even walk the plank... yar cut off!"
            break

        if len(customers[customer_name]["regDrinkIngredients"]) > 1:
            customers[customer_name]["numDrunk"] += 1
            print '\nHere be yer', customers[customer_name]["regDrinkName"]
            for i in customers[customer_name]["regDrinkIngredients"]:
                print " -", i
        else:
            print "\nYar a picky one!  No drink for ye, then."
            break

        while True:
            print
            another = raw_input('Would ye like another? ')
            if another.lower() in ("y", "yes", "n", "no"):
                break

        if another.lower() in ("n", "no"):
            print ("\nOff with ye then, ye scallywag!")
            break

    return


if __name__ == '__main__':

    drink_style_dict = {}

    while True:
        customer_name = raw_input("\nAhoy thar... what be yar name? ")
        if customer_name not in customers:
            print "\nWell, " + customer_name + "... let's find a new drink for ye!"
            customers[customer_name] = {}
            customers[customer_name]["numDrunk"] = 0
            customers[customer_name]["regDrinkName"] = random.choice(adjectives) + " " + random.choice(nouns)
            customers[customer_name]["regDrinkIngredients"] = construct_drink(get_drink_style(drink_style_dict))

        serve_customer(customer_name)

        while True:
            print
            another = raw_input('Is thar another customer to serve? ')
            if another.lower() in ("y", "yes", "n", "no"):
                break

        if another.lower() in ("n", "no"):
            print ("\nI'm closing up, then... be gone with ye all!")
            break
