$(function() {
    console.log("dom is ready!");

    $(".retry").hide()
    $(".new-link").hide()


    $('#post-form').on('submit', function(event){
   //      event.PreventDefault;
           console.log("yay!")
           value = $('input[name="ingredient"]').val();
           console.log(value)
   //      $('#top').hide()
         $.ajax({
            type: "POST",
            url: "/",
            data : { ingredient_list : value },
            success: function(result) {
              if (result.recipe_id !== undefined) {
                 console.log(result);
               $(".boom").hide()
               $(".retry").show()
               $(".new-link").show()
               $("#results").html('<h3><a href="http://www.yummly.com/recipe/'+result.recipe_id+'">'+
                   result.recipe_name+'</a></h3><p>Recipe Rating: '+result.recipe_rating+' out of 5</p><br>Ingredients you will need: <ul>'+result.recipe_ingredients+'</ul><a href="http://www.yummly.com/recipe/'+result.recipe_id+
                   '"><img src='+result.recipe_pic+' alt="Recipe photo" style="border-radius:50%;"></a><br><br>');
              } else {
                console.log(result);
                $("#results").html(result.sorry)
            }
            },
            error: function(error) {
                console.log(error);
                $("#errors").html(error.responseJSON.sorry)
            }
        });
    });
    $('.new-link').on('click', function(event){
        event.preventDefault();
        $("input").val('').show();
        $(".boom").show()
        $(".retry").hide()
        $(".new-link").hide()
        $('#results').html('');
    });
});