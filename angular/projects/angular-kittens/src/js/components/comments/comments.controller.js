(function() {

  'use strict';

  angular
    .module('ngKittens.components.comments', [])
    .controller('commentsController', commentsController);

  commentsController.$inject = [];

  function commentsController() {
    /*jshint validthis: true */
    console.log('hi!');
  }

})();
