angular.module('ccApp', ['DataServices', 'Data', 'ngRoute', 'ngAnimate'])

.config(['$locationProvider','$routeProvider',
  function($locationProvider, $routeProvider) {
    $routeProvider
      .when("/home", {
        templateUrl: "./partials/home.html"
      })
      .when("/countries", {
        templateUrl: "./partials/countries.html",
        controller: "countriesController",
      })
      .when("/countries/:countryCode", {
        templateUrl: "./partials/details.html",
        controller: "detailsController",
      })
      .otherwise({
         redirectTo: '/home'
      });
}]);

