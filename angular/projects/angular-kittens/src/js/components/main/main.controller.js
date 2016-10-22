(function() {

  'use strict';

  angular
    .module('ngKittens.components.main', [])
    .controller('mainController', mainController);

  mainController.$inject = ['$rootScope', 'kittensService'];

  function mainController($rootScope, kittensService) {
    /*jshint validthis: true */
    this.kittens = kittensService.getAllKittens();
    this.vote = function(kittenID, type) {
      kittensService.updateLikes(kittenID, type);
    };
  }

})();
