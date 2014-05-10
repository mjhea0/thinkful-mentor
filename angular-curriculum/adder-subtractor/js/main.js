$(function() {

  console.log('ready!');

  // add
  $('#add-btn').click(function(e){
      e.preventDefault()
      value1 = $('#value1').val()
      value2 = $('#value2').val()
      value3 = parseInt(value1) + parseInt(value2)
      $('#addition').html(value3);
      $('#subtract-answer').hide()
      $('#add-answer').show()
  });

  // subtract
  $('#subtract-btn').click(function(e){
      e.preventDefault()
      value1 = $('#value1').val()
      value2 = $('#value2').val()
      value3 = parseInt(value1) - parseInt(value2)
      $('#subtraction').html(value3);
      $('#add-answer').hide()
      $('#subtract-answer').show()
  });

});