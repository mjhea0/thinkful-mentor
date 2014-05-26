$(function() {

  console.log('ready!')

  getValues()

  // on click event ...
  function getValues() {

    $('#add-btn').click(function() {

      // grab values of the inputs
      var item = $('#item-input').val();
      var quantity = $('#quantity-input').val();
      var price = $('#price-input').val();

      // clear out errors/alerts
      $('#alert').html('');

      // ensure no inputs are empty
      if ((item === '') || (quantity === '') || (price === '')) {
        $('#alert').html('<span class="alert-text">All fields are required!</span>'); // if empty
      } else {
        validateValues(item, quantity, price) // if not empty
      };

    });

  };

  // validate values
  function validateValues(itemValue, quantityValue, priceValue) {

    // validate each value with regex
    if (is_valid = !/[^0-9()]+[a-zA-Z]*/.test(itemValue)) { 
      $('#alert').html('<span class="alert-text">The item name must be a string!</span>'); // if invalid
    } else if ((is_valid = !/^[0-9]*(\.[0-9]+)?$/.test(quantityValue)) || 
      (is_valid = !/^[0-9]*(\.[0-9]+)?$/.test(priceValue))) {
      $('#alert').html('<span class="alert-text">The quantity and price must be integers!</span>'); // if invalid
    } else {
      // clear out errors/alerts and inputs
      $('#alert').html('');
      $('#item-input').val('');
      $('#quantity-input').val('');
      $('#price-input').val('');

      var floatPrice = parseFloat(priceValue).toFixed(2);
      var total = calculateTotal(quantityValue, floatPrice)

      // append values to new table row
      $('#my-values').append(
        '<tr><td><input type="checkbox">'+
        '</td><td>'+itemValue+
        '</td><td>'+quantityValue+
        '</td><td>$'+floatPrice+
        '</td><td>$'+total+
        '</td></tr>');

      $('#alert').html('<span class="alert-text">Thanks for adding!</span>').fadeOut(3000); // if empty
    };

    // calculate total
    function calculateTotal(quantityValue, floatPrice) {
      return (quantityValue * floatPrice).toFixed(2)
    };

  };


});

