var myApp = angular.module('myApp', ['ngRoute']);

TEST = 0;

myApp.config(function($routeProvider) {
    $routeProvider
    .when('/', {templateUrl:'partials/home.html'})
    .when('/one', {templateUrl:'partials/one.html', controller:'TestOneController'})
    .when('/two', {templateUrl:'partials/two.html', controller:'TestTwoController'});
});

myApp.controller('TestOneController', function($scope) {
  $scope.value = TEST;
  $scope.addOne = function() {
    console.log("yay!");
    TEST += 1;
    $scope.value = TEST;
  };
});

myApp.controller('TestTwoController', function($scope) {
  $scope.value = TEST;
  $scope.removeTwo = function() {
    console.log("yay!");
    TEST -= 2;
    $scope.value = TEST;
  };
});
