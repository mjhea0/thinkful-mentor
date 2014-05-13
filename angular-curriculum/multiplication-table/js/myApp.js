angular.module('myApp', [])
    .controller('MultiplicationCtrl', function($scope, $attrs) {
      function populateNumbers(x) {
        var numbers = [];
        for(var i=0; i<x; i++) {
          numbers[i] = i + 1; 
        };
        return numbers;
      }

    $scope.compute = function(a,b) {
        return a * b;
    }
    $scope.$watch('numberLimit', function(limit) {
        $scope.numbers = populateNumbers(limit);
    });

    $scope.numberLimit = $attrs.initialNumberLimit || 10;

    var activeFactorA, activeFactorB;
    $scope.setActiveFactors = function(a, b) {
        activeFactorA = a;
        activeFactorB = b;
    };

    $scope.matchesFactor = function (a, b) {
        return a === activeFactorA || b === activeFactorB;
    };
    
    $scope.clearActiveFactors = function() {
      activeFactorA = activeFactorB = null;
    };
  });