$(document).ready(function() {
  /*--- focus on input ---*/
    $("#userGuess").focus();

   /*--- Display information modal box ---*/
    $(".what").click(function(){
        $(".overlay").fadeIn(1000);
    });

    /*--- Hide information modal box ---*/
    $("a.close").click(function(){
        $(".overlay").fadeOut(1000);
    });

    /*--- Start New Game ---*/
    $(".new").click(function() {
        newGame();
    });

    /*---Declare variables---*/
    var numGuesses = 0;
    var diff;
    var guess;
    var finish = false;

    /*---Generate random number and assign to variable---*/
    var target = Math.floor((Math.random() * 100) + 1);
    console.log("The random number is " + target);

    /*--- Accept Guess ---*/
    if (finish === false) {
        $("#guessButton").click(getGuess);
    }
    else {
        $('#feedback').text("You have already won, silly! Please click\"New Game\"");
    }

    $("#userGuess").keyup(function(event) {
        if(event.keyCode == 13){
            $("#guessButton").click();
        }
    });

  /*--- Validate and Process Guess---*/

    function getGuess () {
        guess = +$("#userGuess").val();
        console.log("Guess is " + guess);
        if(!guess || isNaN(guess) || guess <1 || guess >100) {
         $('#feedback').text("You must enter a number between 1 and 100");
         return false;
        }
        else compareGuess(guess);
    }

    function compareGuess(x) {
        diff = Math.abs(x - target);
            if (diff === 0) {
                $('#feedback').text("You guessed correctly! Yay!");
                addGuess();
                finish = true;
                endGame(finish);
            }
            else if (diff < 10) {
                $('#feedback').text("You are getting hotter!");
                addGuess();
            }
            else if (diff < 25) {
                $('#feedback').text("You are sort of warm");
                addGuess();
            }
            else if (diff < 40) {
                $('#feedback').text("You are barely warm");
                addGuess();
            }
            else {
                $('#feedback').text("You are pretty cold");
                addGuess();
            }
       }

     function addGuess() {
       numGuesses++;
        console.log("The number of total guesses is " + numGuesses);
        $('#guessList').append("<li>" + guess + "</li>");
        $('#count').text(numGuesses);
        $("#userGuess").val('');
        $("#userGuess").focus();
     }


    function endGame(finish) {
         $('#guessButton').prop('disabled', finish);
         $('#userGuess').prop('disabled', finish);
    }

    function newGame() {
        numGuesses = 0;
        endGame(false);
        finish = false;
        $('#guessList').children("li").remove();
        target = null;
        guess = null;
        diff = null;
        $('#feedback').text("Welcome!Make your Guess");
        $('#count').text(numGuesses);
        $("#userGuess").val('');
        $("#userGuess").focus();
    }
});