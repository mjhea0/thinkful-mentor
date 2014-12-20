$('#button').click(function() {
  var name = $('#name').val(); // grab input value
  $('#value').html(name); // add data to DOM
  return false; // prevent form submission
});