var app = angular.module("myApp", []);

app.controller('myCtrl', function($scope, foo) {
  $scope.foo = foo;
});

app.factory('foo', function() {
  var privateVariable = "This is private";
  function getPrivateVariable() {
    return privateVariable;
  }

  return {
    publicVariable: "This is public",
    getPrivateVariable: getPrivateVariable
  };
});