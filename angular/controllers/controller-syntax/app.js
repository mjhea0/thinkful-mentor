'use strict';


angular.module('mainApp', [
  'ngRoute',
  'mainApp.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/first', {templateUrl: 'partials/first.html', controller: 'firstCtrl'});
  $routeProvider.when('/second', {templateUrl: 'partials/second.html', controller: 'secondCtrl'});
  $routeProvider.otherwise({redirectTo: '/'});
}]);