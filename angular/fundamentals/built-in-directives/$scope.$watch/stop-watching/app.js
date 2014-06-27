var app = angular.module('app', []);

app.controller('MainController', function($scope) {

    $scope.number = 0
    $scope.numArray = []

  $scope.increment = function() {
    $scope.number++;
  }

  $scope.stop = $scope.$watch('number', function() {
    $scope.numArray.push($scope.number)
  })

});
