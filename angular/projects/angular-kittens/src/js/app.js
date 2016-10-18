(function() {

  'use strict';

  angular
    .module('ngKittens', [
      'ngRoute',
      'ngKittens.config',
      'ngKittens.services',
      'ngKittens.components.main',
      'ngKittens.components.kittens',
      'ngKittens.components.comments'
    ]);

})();
