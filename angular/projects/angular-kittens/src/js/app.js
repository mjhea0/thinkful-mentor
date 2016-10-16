(function() {

  'use strict';

  angular
    .module('ngKittens', [
      'ngRoute',
      'ngKittens.config',
      'ngKittens.components.main',
      'ngKittens.components.kittens'
    ]);

})();
