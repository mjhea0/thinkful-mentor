var myApp = angular.module('myApp', ['ngRoute']);

myApp.controller('WidgetsController', function($scope) {});
myApp.controller('MyCtrl', function($scope, $location) {
    $scope.isActive = function(route) {
        return route === $location.path();
    }
});


myApp.config(function($routeProvider) {

    $routeProvider
    .when('/one', {templateUrl:'partials/one', controller:'WidgetsController'})
    .when('/two', {templateUrl:'partials/two', controller:'WidgetsController'})

});
