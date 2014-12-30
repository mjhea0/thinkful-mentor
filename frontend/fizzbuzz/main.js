$(function() {

  // sanity check
  console.log('working!')

  // event handler
  $('#submit-button').on('click', function() {

    // sanity check
    console.log("event is handled!")

    // grab values
    var startingValue = $("#starting-value").val()
    var endingValue = $("#ending-value").val();

    // create array
    var results = createArray(startingValue, endingValue)

    // console.log(results)
    alert(results)

  });

  function createArray(start, end) {

    // container for results
    var resultsArray = []

    // loop through starting and ending values
    for (var i = start; i <= end; i++) {

      if (i % 3 == 0) {
        result = "Fizz";
      } else if (i % 5 == 0) {
        result = "Buzz";
      } else {
        result = i;
      };

      // add individual result to array
      resultsArray.push(result)

    };
    return resultsArray;
  };

});