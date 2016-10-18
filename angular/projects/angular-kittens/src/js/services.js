(function() {

  'use strict';

  angular
    .module('ngKittens.services', [])
    .service('kittensService', kittensService);

  function kittensService() {
    /*jshint validthis: true */
    const kittens = [
      {
        id: 1,
        name: 'Robby',
        bio: 'eats like a deer',
        likes: 0,
        url: 'https://placekitten.com/g/100/100',
        comments: [
          'So nice',
          'Is that hajek?'
        ]
      }
    ];
    this.getAllKittens = function() {
      return kittens;
    };
    this.addKitten = function(kitten) {
      kittens.push(kitten);
    };
    this.getNextID = function() {
      return parseInt(kittens[kittens.length - 1].id) + 1;
    };
  }

})();
