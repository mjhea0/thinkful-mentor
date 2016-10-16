(function() {

  'use strict';

  angular
    .module('ngKittens.components.kittens', [])
    .controller('kittensController', kittensController);

  kittensController.$inject = ['$rootScope', '$location'];

  function kittensController($rootScope, $location) {
    /*jshint validthis: true */
    if (!$rootScope.kittens) {
      $rootScope.kittens = [];
    }
    this.kitten = init();
    this.addKitten = function() {
      this.kitten.likes = 0;
      $rootScope.kittens.push(this.kitten);
      this.kitten = init();
      $location.path('/');
    };
  }

  function init() {
    const kitten = {};
    kitten.url = 'https://placekitten.com/g/200/300';
    return kitten;
  }

})();
