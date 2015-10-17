import random

# globals

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


# functions

def drink_pref():
    """I collect the user's drink pref and put it into a new dictionary"""
    preferences = {}
    for key, value in questions.items():
        user_input = input(value + " ")
        preferences[key] = (user_input == "y" or user_input == "yes")
    return preferences


def mix_the_drink(value):
    """I now use the user preferences captured in the responses dict
    and make a delicious drink"""
    my_drink = []
    for key, value in value.items():
        if value is True:
            my_drink.append(random.choice(ingredients[key]))
    return my_drink


# main

def main():
    results = drink_pref()
    print("\nGreat! Based on your choices, I recommend a cocktail with a:")
    for drink in mix_the_drink(results):
        print("    " + drink)


if __name__ == "__main__":
    main()
