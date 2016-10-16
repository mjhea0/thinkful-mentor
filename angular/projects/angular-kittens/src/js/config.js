(function() {

  'use strict';

  angular
    .module('ngKittens.config', [])
    .config(appConfig);

  function appConfig($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'js/components/main/main.view.html',
        controller: 'mainController',
        controllerAs: 'mainCtrl'
      })
      .when('/new', {
        templateUrl: 'js/components/kittens/kittens.view.html',
        controller: 'kittensController',
        controllerAs: 'kittensCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  }

})();
