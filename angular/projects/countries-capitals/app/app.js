'use strict';

angular.module('CountriesCapitalsApp', ['DataServices', 'ngRoute', 'ngAnimate'])

.constant('VERSION', "0.1")

.config([
    '$locationProvider',
    '$routeProvider',
    function($locationProvider, $routeProvider) {
        $locationProvider.hashPrefix('!');
        // routes
        $routeProvider
            .when("/", {
                templateUrl: "./home/home.html"
            })
            .when("/countries", {
                templateUrl: "./countries/countries.html",
                controller: "CountriesController"
            })
            .when("/countries/:countryCode", {
                templateUrl: "./countries/country.html",
                controller: 'CountryController'
            })
            .otherwise({
                redirectTo: '/'
            });
    }
]);
