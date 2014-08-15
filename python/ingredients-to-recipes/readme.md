## ingredients -> recipes

Given a list of ingredients, provide a list of recomendations

### Research API

- Determine what data you can get from the API from the [documentation](https://developer.yummly.com/documentation)
- Which endpoints will you be using?
    - Ingredient: Given a user inputed ingredient, you need to see if it is valid.
    - Recipes: With a list of ingredients, you then need to search for recipes.
- Problems: Is 'chicken breast' the same as 'chicken breasts', 'Chicken breast', 'breast of chicken', etc.? How are you going to take the user input so that if someone enters 'Chicken breasts' it won't turn up 0 ingredients if there is an ingredient called 'chicken breast' in the API? Possible solution: When user searches for 'onion', the response is a list of similar ingredients - like onion, onions, yellow onion, red onion, red onions, etc. - and then the user picks the ingredient from that list.

### TDD

1. Start simple
1. Write a test - when user hits the main URL ('/'), a search form is populated
1. Write code to pass test
1. Write a test - when the user submits an ingredient, a list of similar ingredients are displayed (in the test you will have to mock out the actual API call)
1. Write code to pass test - after form submission, grab the entered ingredient, pass the ingredient to the API call, grab the returned data and add it to the DOM
1. Rinse, repeat