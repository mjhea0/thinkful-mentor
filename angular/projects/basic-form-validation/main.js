var app = angular.module('formApp', [])

app.controller('formController', function($scope) {

  $scope.user = {}
  $scope.isValid = false
  $scope.submitted = false

  $scope.save = function() {
    $scope.submitted = true
    if ($scope.userForm.$valid) {
      $scope.isValid = true
    }
  }

});