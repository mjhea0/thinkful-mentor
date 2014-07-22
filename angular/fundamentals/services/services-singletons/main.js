var app = angular.module('myApp', [])

app.service('foo', function() {
  console.log(this)
});

app.controller('firstCtrl', function(foo) {
  var a = foo;
  var b = foo;
  console.log("Are they equal?", a===b)
});

app.controller('secondCtrl', function(foo) {
  // empty
});

app.factory('bar', function() {
  console.log(this)
});

app.controller('thirdCtrl', function(bar) {
  // empty
});

app.controller('fourthCtrl', function(bar) {
  // empty
});
