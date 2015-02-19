angular.module('myApp', [])


.controller("myTableCtrl", ['$scope', '$attrs', function ($scope, $attrs) {

  $scope.numberLimit = $attrs.initialNumberLimit || 10;

  function populateNumbers(limit) {
    var numbers = [];
    for (var i = 0; i < limit; i++) {
      numbers[i] = i + 1;
    }
    return numbers;
  }

  $scope.compute = function (a, b) {
     return a * b;
  };

  $scope.$watch('numberLimit', function(limit) {
    $scope.numbers = populateNumbers($scope.numberLimit);
  });

}]);