var app = angular.module('app', []);

app.controller('MainController', function($scope) {
  $scope.myData = {val: "Michael"}

  $scope.$watch('myData.val',function(newval) {
    $scope.myData.toolong = newval.length > 15
  })
})
