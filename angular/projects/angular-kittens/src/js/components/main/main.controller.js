(function() {

  'use strict';

  angular
    .module('ngKittens.components.main', [])
    .controller('mainController', mainController);

  mainController.$inject = ['$rootScope', 'kittensService'];

  function mainController($rootScope, kittensService) {
    /*jshint validthis: true */
    this.kittens = kittensService.getAllKittens();
    this.orderBy = 'likes';
    this.orderBySymbol = '-';
    this.order = this.orderBySymbol + this.orderBy;
    this.changeOrder = function(by) {
      if (by === 'name') {
        this.orderBy = 'name';
        if (this.orderBySymbol === '+') {
          this.orderBySymbol = '-';
        } else {
          this.orderBySymbol = '+';
        }
      }
      if (by === 'likes') {
        this.orderBy = 'likes';
        if (this.orderBySymbol === '+') {
          this.orderBySymbol = '-';
        } else {
          this.orderBySymbol = '+';
        }
      }
      this.order = this.orderBySymbol + this.orderBy;
      console.log(this.order);
    };
    this.vote = function(kittenID, type) {
      kittensService.updateLikes(kittenID, type);
    };
  }

})();
