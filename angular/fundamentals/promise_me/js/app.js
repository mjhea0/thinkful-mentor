var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope, $q, $timeout) {
  $scope.mydata = 1;
  $scope.mydata2 = 2;
  $scope.mydata3 = 3;
  var defer = $q.defer();
  var defer2 = $q.defer();
  var defer3 = $q.defer();

  $scope.secret = function () {
    console.log("secret function fired");
    defer.promise.then(function(val) {
      $scope.mydata = val;
      console.log($scope.mydata2);
    });
    defer2.promise.then(function(val) {
      $scope.mydata2 = val;
      console.log($scope.mydata3);
    });
    defer3.promise.then(function(val) {
      $scope.mydata3 = val;
      console.log($scope.mydata);
    });

    $timeout(function() {
      console.log("First defer resolved!");
      defer.resolve("I");
    }, 1000);
    $timeout(function() {
      console.log("Second defer resolved!");
      defer2.resolve("keep");
    }, 2000);
    $timeout(function() {
      console.log("Third defer resolved!");
      defer3.resolve("promises");
    }, 3000);
  };
});



