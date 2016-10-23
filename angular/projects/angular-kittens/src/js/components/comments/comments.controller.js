(function() {

  'use strict';

  angular
    .module('ngKittens.components.comments', [])
    .controller('commentsController', commentsController);

  commentsController.$inject = ['$routeParams', 'kittensService'];

  function commentsController($routeParams, kittensService) {
    /*jshint validthis: true */
    this.kittenID = $routeParams.id;
    this.kittenName = kittensService.getName($routeParams.id);
    this.comments = kittensService.getComments($routeParams.id);
    this.comment = '';
    this.showForm = function () {
      this.isVisible = true;
    };
    this.hideForm = function () {
      this.isVisible = false;
      this.comment = '';
    };
    this.addComment = function() {
      kittensService.addComment($routeParams.id, this.comment);
      this.isVisible = false;
      this.comment = '';
    };
  }

})();
