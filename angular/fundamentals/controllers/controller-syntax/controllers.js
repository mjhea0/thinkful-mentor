'use strict';

/* Controllers */

angular.module('mainApp.controllers', [])
  .controller('firstCtrl', ['$scope', function($scope) {
    $scope.val = "123"
  }])
  .controller('secondCtrl', ['$scope', function($scope) {
    $scope.val = "456"
  }]);