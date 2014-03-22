$(function() {
  console.log("ready!");

  //show open_table table on button click
  $(".open_label").on('click',function(){
    $("#open_table").show()
    $(".hide_label").show()
    $("#closed_table").hide()
  });
  
  //show closed_table table on button click
  $(".closed_label").on('click',function(){
    $("#closed_table").show()
    $(".hide_label").show()
    $("#open_table").hide()
  });

  //hide all tables on button click
  $(".hide_label").on('click',function(){
    $("#closed_table").hide()
    $("#open_table").hide()
    $(".hide_label").hide()
  });

  // unselect period when mode is selected
  $("#mode-group .btn").on('click',function(){
    $("#period-group").button('reset');
  });
  
});



