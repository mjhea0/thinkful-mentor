$(function() {
  console.log('ready!');
});

angular.module('ngMadlibs', [])
  .controller('madlibsController', function($scope) {
    $scope.newValue = function(value) {
      if (value === "male") {
        $('#male-text').show()
        $('#female-text').hide()
      } else if (value === "female") {
        $('#female-text').show() 
        $('#male-text').hide()
      }
    }
    $scope.add = function() {
      $scope.items = [
        { name: 'foo' },
        { name: 'bar' },
        { name: 'blah' }
      ];
      console.log($scope.male)
      console.log($scope.menu)
    };
  });