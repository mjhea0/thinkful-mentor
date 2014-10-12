$(function() {

    console.log("dom is ready!");

    $(".another").hide()
    $(".new-link").hide()

    $('#post-form').on('submit', function(){

        console.log("yay!") // sanity check
        formValue = $('input[name="ingredient"]').val(); // grab form value

        $.ajax({
            type: "POST",
            url: "/",
            data : { ingredient_list: formValue },
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
            error: function(error) {
                console.log(error.responseJSON)
                $("#results").html('<h3>'+error.responseJSON.error+'</h3>');
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