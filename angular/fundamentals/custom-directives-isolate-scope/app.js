var app = angular.module('isolateScopeExample', []);

app.controller('myController', function ($scope) {
  $scope.name = 'Michael';
  $scope.color = '#000000';
  $scope.reverse = function () {
    $scope.name = $scope.name.split('').reverse().join('');
  };
});

app.directive('isolateScope', function () {
  return {
    scope: {
      name: '@',
      color: '=',
      reverse: '&'
    },
    templateUrl: 'test.html'
  };
});