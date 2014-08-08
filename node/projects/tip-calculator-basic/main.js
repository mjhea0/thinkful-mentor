window.onload=function(){

  // prompt user for inputs, assign to variables
  var base = parseFloat(prompt("How much was your meal?"));
  var tax = parseFloat(prompt("What is the tax rate? (enter 10 for 10%)"));
  var tip = parseFloat(prompt("What percentage would you like to tip? (enter 10 for 10%)"));

  // calculate totals
  var tipValue = (tip / 100) * base;
  var subtotal = base + tipValue;
  var taxValue = (tax / 100) * subtotal;
  var total = subtotal + taxValue;


  // build alert message
  var headerMessage = "MEAL DETAILS\n" +
                      "------------------\n";

  var costMessage = "Base Price: $"       + base.toFixed(2) +
                    "\nTip Percentage: "  + tip.toFixed(2) + "%" +
                    "\nTip value: $"      + tipValue.toFixed(2) +
                    "\nTax Percentage: "  + tax.toFixed(2) + "%" +
                    "\nTax value: $"      + taxValue.toFixed(2);

  var totalMessage = "\n------------------\n" +
                     "Total Cost: $ " + total.toFixed(2);

  alert(headerMessage + costMessage + totalMessage);

}