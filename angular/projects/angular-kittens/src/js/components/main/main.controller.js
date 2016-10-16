(function() {

  'use strict';

  angular
    .module('ngKittens.components.main', [])
    .controller('mainController', mainController);

  mainController.$inject = ['$rootScope'];

  function mainController($rootScope) {
    /*jshint validthis: true */
    if (!$rootScope.kittens) {
      $rootScope.kittens = [];
    }
  }

})();
