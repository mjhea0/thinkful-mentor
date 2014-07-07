var app = angular.module('myApp', []);

app.controller('appController', function($scope, $q, $timeout) {

  $scope.mydata = "Hello, "

  var defer = $q.defer();

  defer.promise
    .then(function(val) {
      $scope.mydata += val
      return val
    })

  $timeout(function() {
    defer.resolve("World!");
  },3000)
});
