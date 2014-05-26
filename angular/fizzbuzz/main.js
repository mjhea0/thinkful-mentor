angular.module('myApp', []).
  controller('myCtrl', function($scope) {
    function range(start, stop, step){
    var a=[start], b=start;
    while(b<stop){b+=step;a.push(b)}
    return a;
    };
      $scope.numbers = range(1, 100, 1);
  });