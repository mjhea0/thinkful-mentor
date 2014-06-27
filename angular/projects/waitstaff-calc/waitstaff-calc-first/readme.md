## Assignment

There are three main components to the interface. Here's how each one should work:

1. Meal Details: In the left most panel, the user enters the base cost for a meal, the tax rate, and the tip percentage the customer wants to leave. When they hit the submit button, the app should validate that the value in each field is numeric. If the form is valid, the Customer Charges and My Earnings Info section should update accordingly.

1. Customer Charges: This panel displays what the customer should be charged. Subtotal is the value of the base meal price plus tax. Tip is dollar value of the tip, given the subtotal and tip percentage. Total is equal to subtotal plus tip.

1. My Earnings Info: This panel displays cumulative information about all of the meals submitted so far. Tip-total is the sum of all tips computed so far. Meal count is the total number of meals input into the tool. Average tip per meal is equal to the total tip value divided by the number of meals.

1. Note the "Reset" button in the bottom right of the interface. When the user clicks this button, the app should return to its initial state. All of the cumulative info should reset.

**I updated the section names and changed the functionality of the "Reset" button.**

## URL

1. http://www.realpython.com/learn/waitstaff-calc/
2. http://www.realpython.com/learn/waitstaff-calc-mobile/

## To do

1. Form validation

  Form validation does not work right. When the type is set to "number", if you enter a non-number, the form thinks the input is empty. How to fix - set the type to text, write function to convert to int, handle errors appropriately.

  Or regex - `<input type="text" pattern="\d*">` ?

  **Update**: Ripped out Angular validation, let HTML5 handle it. (look into this - http://www.html5rocks.com/en/tutorials/forms/constraintvalidation/)

2. Add local storage