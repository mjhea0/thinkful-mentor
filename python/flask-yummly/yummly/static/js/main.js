$(function() {

    console.log("dom is ready!");
    $(".another").hide()
    $(".new-link").hide()

    $('#post-form').on('submit', function(event){
        event.PreventDefault;
        console.log("yay!")
        $.ajax({
            type: "POST",
            url: "/",
            data : { ingredient_list : $('.ingredients').val() },
            success: function(recipe) {
                $("input").hide()
                $(".boom").hide()
                $(".another").show()
                $(".new-link").show()
                console.log(recipe);
                $("#results").html('<h3><a href="http://www.yummly.com/recipe/'+recipe.recipe_id+'">'+
                    recipe.recipe_name+'</a></h3><br><a href="http://www.yummly.com/recipe/'+recipe.recipe_id+
                    '"><img src='+recipe.recipe_pic+' alt="Recipe photo" style="border-radius:50%;"></a><br><br>');
            },
            error: function() {
                console.log("yikes")
            }
        });
    });

    $('.new-link').on('click', function(event){
        event.preventDefault();
        $("input").val('').show();
        $(".boom").show()
        $(".another").hide()
        $(".new-link").hide()
        $('#results').html('');
    });

});