
$(document).ready(function(){
	console.log("dom is ready!");
	$("#list").hide();

	var randomNumber=Math.floor(Math.random()*101);

	function getRandomNumber(){
		console.log ("Random number = " + randomNumber);
	}

	function startNewGame(){
		console.log("Starting over...");
		var value = 0;
		$("#list").hide();
		$("#guessList").empty();
		$("#feedback").text("Make your Guess!");
		$("#count").html(value);

	}

	/*--- Display information modal box ---*/
  	$(".what").click(function(){
    	$(".overlay").fadeIn(1000);

  	});

  	/*--- Hide information modal box ---*/
  	$("a.close").click(function(){
  		$(".overlay").fadeOut(1000);
  	});
	// New game
	$(".new").click(function(){
		startNewGame();
	});

  	// Check guess from user
  	document.getElementById('guessButton').onclick = function play(){
  		event.preventDefault();

  		console.log("Guess button working");
		getRandomNumber();
		var guess = $('input[name="userGuess"]').val();
  		console.log(guess);
  		var Diff = Math.abs(randomNumber - guess);

  		if (!guess || isNaN(guess) || guess <1 || guess >100) {
			alert("Your guess must be a number between 1 and 100. Try again.")
			return false;
		}

		else if (Diff > 0 && Diff <= 10) {
			console.log("very close!");
			$("#feedback").text("You are on fire!!");
		}

		else if (Diff > 30 && Diff <= 50) {
			$("#feedback").text("You are cold.");
		}

		else if (Diff > 20 && Diff <= 30) {
			$("#feedback").text("You are warm.");
		}

		else if (Diff > 10 && Diff <= 20) {
			$("#feedback").text("You are getting hot!");
		}

		else if (Diff > 50) {
			$("#feedback").text("You are ice cold.");
		}

		else {
			$("#feedback").text("You win! Click 'New Game' to play again.");
		}

  		var value = parseInt($('#count').html());
  		value++;
  		$("#count").html(value);
  		$("#list").show();
  		$("#guessList").append(guess + ', ');
  		$("#userGuess").val("");
  	}
});



