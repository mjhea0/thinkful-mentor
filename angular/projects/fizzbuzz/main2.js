angular.module('myApp', []).
  controller('myCtrl', function($scope) {

    var test = []

    function range(start, stop, step){
      var a=[start], b=start;
      while(b<stop){b+=step;a.push(b)}
      return a;
    };

    var numberRange = range(1, 100, 1)

    for (var i = 0; i < numberRange.length; i++) {
      if (numberRange[i] % 15 === 0) {
        test.push("FizzBuzz")
      } else if (numberRange[i] % 5 === 0) {
        test.push("Buzz")
      } else if (numberRange[i] % 3 === 0) {
        test.push("Fizz")
      } else {
        test.push(numberRange[i])
      }
    };

    console.log(test)

     $scope.numbers = test

  });