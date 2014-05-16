$(function() {
  console.log('ready!');
});

angular.module('ngMadlibs', [])
  .controller('madlibsController', function($scope) {
    $scope.add = function() {
      console.log($scope.name)
    };
  });