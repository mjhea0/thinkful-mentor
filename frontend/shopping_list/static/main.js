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
        $('#alert').html('<span class="alert alert-danger">All fields are required!</span>'); // if empty
      } else {
        validateValues(item, quantity, price) // if not empty
      };

    });

  };

  // validate values
  function validateValues(itemValue, quantityValue, priceValue) {

    // validate each value with regex
    if (is_valid = !/[^0-9()]+[a-zA-Z]*/.test(itemValue)) { 
      $('#alert').html('<span class="alert alert-danger">The item name must be a string!</span>');
    } else if ((is_valid = !/^[0-9]*(\.[0-9]+)?$/.test(quantityValue)) || 
      (is_valid = !/^[0-9]*(\.[0-9]+)?$/.test(priceValue))) {
      $('#alert').html('<span class="alert alert-danger">The quantity and price must be integers!</span>');
      // clear out errors/alerts
    } else {
      $('#alert').html('');
      // append values to new table row
      $('#my-values').append('<tr><td>'+itemValue+'</td><td>'+quantityValue+'</td><td>'+priceValue+'</td></tr>');
      };
  };

});