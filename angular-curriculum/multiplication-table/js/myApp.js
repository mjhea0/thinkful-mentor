angular.module('myApp', [])
  .controller('DisplayCtrl', function($scope) {
    $scope.$on('displayData', function(event, data) {
      $scope.content = data;
    });
  })

  .controller('MultiplicationCtrl', function($scope, $attrs, $rootScope) {
    function populateNumbers(x) {
      var numbers = [];
      for(var i=0; i<x; i++) 
        {numbers[i] = i + 1; };
        return numbers;
    }

    $scope.compute = function(a,b) {
       return a * b;
    };

    $scope.$watch("numberLimit", function(limit) {
      $scope.numbers = populateNumbers(limit);
    });

    $scope.numberLimit = $attrs.initialNumberLimit || 10;
    
    var activeFactorA, activeFactorB;
    $scope.setActiveFactors = function(a, b) {
      activeFactorA = a;
      activeFactorB = b;
    };

    $scope.matchesFactor = function(a, b) {
      return a === activeFactorA || b === activeFactorB;
    };
    
    $scope.setActiveNumber = function(number) {
      $rootScope.$broadcast('displayData', number);
      console.log("Clicked number is: ", number)
    };
      
    $scope.clearActiveFactors = function() {
      activeFactorA = activeFactorB = null;
    };
  });
