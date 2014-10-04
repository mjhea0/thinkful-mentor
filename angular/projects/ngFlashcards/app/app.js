(function () {

  'use strict';

  angular.module('ngFlashcards', [])

  .controller('mainController', ['$scope', function($scope) {

    // globals
    function init(){
      $scope.hasStarted = false;
      $scope.currentCardNum = 0;
      $scope.activeCardsExist = true;
      $scope.currentCard = 0;
    }

    init();

    $scope.activeCards = [
      {"id": 1, "question": "Do you like Angular?", "choices": ["yes", "no"], "answer": "yes", "isCorrect": false},
      {"id": 2, "question": "Do you like JavaScript?", "choices": ["yes", "no"], "answer": "no", "isCorrect": false},
      {"id": 3, "question": "Do you like python?", "choices": ["yes", "no"], "answer": "yes", "isCorrect": false}
    ];

    // start and end quiz
    $scope.startQuiz = function(){
      $scope.hasStarted = true;
      $scope.activeCards.unshift($scope.currentCard);
      $scope.currentCard = $scope.activeCards.pop();
    };
    $scope.endQuiz = function(){
      location.reload(true);
    };

    // grade, show next card
    $scope.gradeCurrentCard = function(){
      if ($scope.answer == $scope.currentCard.answer) {
        console.log("yay!");
      } else {
         console.log("no!");
      }
      $('input').attr('checked',false);
      $scope.activeCards.unshift($scope.currentCard);
      $scope.currentCard = $scope.activeCards.pop();

    };

    // get answer
    $scope.getChoice = function(choice){
      $scope.answer = choice;
    };

  }]);

}());