angular.module("SettingsModule", ["ngRoute"])
  .config(function($routeProvider) {
    $routeProvider.when('/settings', {
      controller : "SettingsCtrl",
      templateUrl : "settings.html",
      resolve : {
        currentUser : function($http) {
          return $http.get("/api/current-user");
        }
      }
    });
  })
  .controller("SettingsCtrl", function($rootScope, currentUser) {
    $rootScope.page = 'settings';
  });