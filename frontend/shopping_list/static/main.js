$(function() {

  console.log('ready!')

  getValues()

  // handle button click
  $('#add-btn').click(function() {

    // grab values of the inputs
    var item = $('#item-input').val();
    var quantity = $('#quantity-input').val();
    var price = $('#price-input').val();

    // clear out errors/alerts
    $('#alert').html('<br>');

    // ensure no inputs are empty
    if ((item === '') || (quantity === '') || (price === '')) {
      // if empty
      $('#alert').html('<span class="alert-text">All fields are required!</span>');
    } else {
      // if not empty
      validateValues(item, quantity, price)
    };

  });


  // validate values
  function validateValues(itemValue, quantityValue, priceValue) {

    // validate each value with regex
    if (is_valid = !/[^0-9()]+[a-zA-Z]*/.test(itemValue)) { 
      // if invalid
      $('#alert').html('<span class="alert-text">The item name must be a string!</span>');
    } else if ((is_valid = !/^[0-9]*(\.[0-9]+)?$/.test(quantityValue)) || 
      // if invalid
      (is_valid = !/^[0-9]*(\.[0-9]+)?$/.test(priceValue))) {
      $('#alert').html('<span class="alert-text">The quantity and price must be integers!</span>');
    } else {
      // if valid

      // clear out errors/alerts and inputs
      $('#alert').html('');
      $('#item-input').val('');
      $('#quantity-input').val('');
      $('#price-input').val('');

      // convert priceValue to float
      var floatPrice = parseFloat(priceValue).toFixed(2);

      // calculate total
      var total = calculateTotal(quantityValue, floatPrice)

      // convert data to a object
      data = {
        'id': new Date().getTime(),
        'name':itemValue,
        'quantity':quantityValue,
        'price':floatPrice,
        'total':total,
        'complete':0, 
      }

      // test to see if there are any items in storage
      if (localStorage.listSize == undefined ) {
        // if not, set list size (number of items in storage) to 0
        localStorage.setItem('listSize', 0)
      };

      // update list size
      var listSize = parseInt(localStorage.listSize) + 1;

      // pass the current size, plus the object to the `addValuesToStorage()` function
      addValuesToStorage(listSize, data)

      // call the `getValues()` function to get new data
      getValues()

    };


    // calculate total
    function calculateTotal(quantityValue, floatPrice) {
      return (quantityValue * floatPrice).toFixed(2)
    };


    // add values to local storage
    function addValuesToStorage(listSize, data) {

      // create unique id
      var key = 'item_' + listSize;
      localStorage.setItem('listSize', listSize);

      // add to storage
      localStorage.setItem(key, JSON.stringify(data));

    }

  };


  // append values to the dom
  function appendValue(listRow, number) {

    if (listRow.complete === 0) {
      // append values to incomplete table
      $('#my-values').append(
        '<tr><td><input type="checkbox" class="checkbox" id="item_'+(number-1)+'">'+
        '</td><td>'+listRow.name+
        '</td><td>'+listRow.quantity+
        '</td><td>$'+listRow.price+
        '</td><td>$'+listRow.total+
        '</td></tr>');
    } else {
      // append values to complete table 
      $('#my-complete-values').append(
        '<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;'+
        '</td><td>'+listRow.name+
        '</td><td>'+listRow.quantity+
        '</td><td>$'+listRow.price+
        '</td><td>$'+listRow.total+
        '</td></tr>');
    }

  $('#alert').html('<br>');

  };


  // grab id of the checkbox when clicked
  $('.checkbox').change(function(){

    elementId = $(this).attr('id')

    var grabItem = localStorage.getItem(elementId)

    // update complete value to 1
    data = jQuery.parseJSON(grabItem)
    data["complete"] = 1

    // remove element from dom
    $('#'+elementId).remove()

    // update storage
    localStorage.removeItem(elementId);
    localStorage.setItem(elementId, JSON.stringify(data));

    // call the `getValues()` function to get new data
    getValues()

  });


  // get values from local storage
  function getValues() {

    // test to see if there are any items in storage
    var listCount = JSON.parse(localStorage.getItem("listSize"));

    // if so - loop through them, passing each to the `appendValue()` function
    if (localStorage.listSize != undefined ) {
      for (i=1;i<=listCount;i++) {
        var number = parseInt(i) + 1;
        var listRow = jQuery.parseJSON(localStorage.getItem("item_" + i));
        appendValue(listRow, number)
      };
    };
  };

  $('#complete-btn').click(function() {
    $('#complete-items').toggle();
    $('#incomplete-items').hide();
  });

  $('#incomplete-btn').click(function() {
    $('#incomplete-items').toggle();
    $('#complete-items').hide();
  });


});

