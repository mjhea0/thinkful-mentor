angular.module('angularFlashcards')
  .factory('Cards', function () {
    var Cards = [
      {"question": "Do you like me?", "options":["Yes", "No", "Maybe"], "answer": "Yes", "chosenOption": ""},
      {"question": "Do you NOT like me?", "options":["Yes", "No", "Maybe"], "answer": "No", "chosenOption": ""}
    ];
    return Cards;
  });