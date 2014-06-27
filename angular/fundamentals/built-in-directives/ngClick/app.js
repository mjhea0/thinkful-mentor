var app = angular.module('app', []);

app.controller('MainController', function($scope) {
    $scope.val = 0
    $scope.increment = function() {
      $scope.val += 1
    }
})
