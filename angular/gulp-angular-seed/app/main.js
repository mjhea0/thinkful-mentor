(function () {

   'use strict';


    angular.module('SampleApp', ['ngRoute', 'ngAnimate'])

    .constant('VERSION', "0.1")

    .config([
        '$locationProvider',
        '$routeProvider',
        function($locationProvider, $routeProvider) {
            $locationProvider.hashPrefix('!');
            // routes
            $routeProvider
                .when("/", {
                    templateUrl: "./templates/home.html",
                    controller: "MainController"

                })
                .otherwise({
                    redirectTo: '/'
                });
        }
    ]);

    //Load controller
    angular.module('SampleApp')

    .controller('MainController', [
        '$scope',
        function($scope) {
           $scope.test = "Testing Routes!";
        }
    ]);


}());


