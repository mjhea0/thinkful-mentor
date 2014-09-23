(function () {

  'use strict';

  angular.module('ngFlashcards', [])

  .controller('mainController', ['$scope', function($scope) {

    console.log("test");
    $scope.test = "hiya";

    $scope.cards = [
        {"question": "Do you like Angular?", "answer": "Yes"},
        {"question": "Do you like JavaScript?", "answer": "No"}
    ]

  }]);

}());