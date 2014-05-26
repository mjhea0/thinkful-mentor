$(function() {

  console.log('ready!')

  // on click event ...
  $('#add-btn').click(function() {

    // grab values of the inputs
    var item = $('#item-input').val();
    var quantity = $('#quantity-input').val()
    var price = $('#price-input').val()

    // append values to new table row
    $('#my-values').append('<tr><td>'+item+'</td><td>'+quantity+'</td><td>'+price+'</td></tr>');

  });

});