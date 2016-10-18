(function() {

  'use strict';

  angular
    .module('ngKittens.components.kittens', [])
    .controller('kittensController', kittensController);

  kittensController.$inject = ['$rootScope', '$location', 'kittensService'];

  function kittensController($rootScope, $location, kittensService) {
    /*jshint validthis: true */
    this.kitten = init();
    this.addKitten = function() {
      this.kitten.likes = 0;
      this.kitten.comments = [];
      this.kitten.id = kittensService.getNextID();
      kittensService.addKitten(this.kitten);
      this.kitten = init();
      $location.path('/');
    };
  }

  function init() {
    const kitten = {};
    kitten.url = 'https://placekitten.com/g/100/100';
    return kitten;
  }

})();
