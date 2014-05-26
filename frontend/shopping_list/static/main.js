$(function() {

  console.log('ready!')

  getValues()

  // on click event ...
  function getValues() {

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

  };

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

      // append values to new table row
      $('#my-values').append(
        '<tr><td><input type="checkbox">'+
        '</td><td>'+itemValue+
        '</td><td>'+quantityValue+
        '</td><td>$'+floatPrice+
        '</td><td>$'+total+
        '</td></tr>');
      $('#alert').html('<br>');
    };

    // calculate total
    function calculateTotal(quantityValue, floatPrice) {
      return (quantityValue * floatPrice).toFixed(2)
    };

  };


});

