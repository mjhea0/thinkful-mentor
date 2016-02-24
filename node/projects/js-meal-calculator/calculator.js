// globals

var currentDiners = parseInt(document.getElementById('diners').innerHTML);
var currentDishes = document.getElementById('dishes').innerHTML;
var total = parseFloat(document.getElementById('total').innerHTML);

// functions

function addDiner() {
  currentDiners++;
  document.getElementById('diners').innerHTML = currentDiners;
}

function addDish() {
  currentDishes++;
  document.getElementById('dishes').innerHTML = currentDishes;
  updateTotal();
}

function updateTotal() {
  total = total + 10;
  document.getElementById('total').innerHTML = total;
}

function checkout() {
  if (currentDiners <= 0 || currentDishes <=0) {
    document.getElementById('receipt').innerHTML = '';
    document.getElementById('receipt').innerHTML = 'Dine and dash alert! No diners (and/or meals) present.';
  } else {
    var totalTaxTip = parseFloat(currentDishes*10*1.1*1.2);
    var dinersOwe = totalTaxTip / currentDiners;
    document.getElementById('receipt').innerHTML = '';
    document.getElementById('receipt').innerHTML = 'The total bill plus 10% tax and 20% tip comes to $' + totalTaxTip.toFixed(2) + ' and each diner owes $' + dinersOwe.toFixed(2);
  }
}