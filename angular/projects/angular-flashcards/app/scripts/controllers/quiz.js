(function () {

  'use strict';

  angular.module('angularFlashcards')

    .controller('QuizCtrl', function ($scope, $interval, Cards) {

      $scope.quiz = Cards; // all cards
      $scope.currentCard = 0;

      $scope.isRunning = false; // quiz is not running
      $scope.timeRemaining = 20; // you have twenty seconds!
      $scope.totalScore = 0;
      console.log($scope.quiz);

      // start quiz!
      $scope.startTimer = function() {
        if ($scope.timeRemaining > 0) {
          $scope.isRunning = true; // quiz is running

          $scope.stopTimer = $interval(function() { // check if quiz is done every second
            $scope.timeRemaining-- ;
            if ($scope.timeRemaining === 0) {
              $interval.cancel($scope.stopTimer);
              $scope.isRunning = false; // quiz is not running
            }
          }, 1000);
        }
      };

      // stop quiz
      $scope.reloadPage = function() {
        $scope.isRunning = false; // quiz is not running
        $scope.timeRemaining = 20; // you have twenty seconds!
        $scope.totalScore = 0;
        $scope.quiz = Cards;
        $interval.cancel($scope.stopTimer);
      };

      // correct!
      $scope.$on('correct!', function() {
        $scope.totalScore += 1;
        $scope.answered = true;
      });

      // incorrect!
      $scope.$on('incorrect!', function() {
        $scope.answered = true;
      });

    });

}());