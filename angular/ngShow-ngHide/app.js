var app = angular.module('app', []);

app.controller('MainController', function($scope) {
    $scope.val = 0
    $scope.isEven = true

    $scope.increment = function() {
      $scope.val += 1
      $scope.isEven = $scope.val % 2 == 0
    }
})
