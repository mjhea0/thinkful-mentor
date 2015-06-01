angular.module('weatherApp', ['ngRoute', 'dataServices','ngAnimate','directives','ngAutocomplete'])

.config(['$locationProvider','$routeProvider',
  function($locationProvider, $routeProvider) {
    $routeProvider
      .when("/home", {
        templateUrl: "/partials/home.html",
        controller: "mainCtrl",
    })
      .otherwise({
         redirectTo: '/home'
      });
}])

.filter('percentage', ['$filter', function ($filter) {
  return function (input, decimals) {
    return $filter('number')(input * 100, decimals) + '%';
  };
}]);