$(function() {

  console.log('ready!');



});



angular.module('ngMadlibs', [])
  .controller('madlibsController', function ($scope) {
    $scope.newValue = function(value) {
     console.log(value);
      if (value === "male") {
        $('#inputs').show()
        $('#male-text').show()
        $('#female-text').hide()
      } else if (value === "female") {
        $('#inputs').show()
        $('#female-text').show() 
        $('#male-text').hide()
      }
    }
  });


