(function () {

  'use strict';

  angular.module('angularFlashcards')

    .controller('QuestionCtrl', function ($scope) {

      $scope.checkAnswer = function(quiz) {
        console.log(quiz);
        if (quiz.chosenOption === quiz.answer) {
          $scope.$emit('correct!');
        } else {
          $scope.$emit('incorrect!');
        }
      };

    });

}());
