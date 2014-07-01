var app = angular.module('animateApp', ['ngAnimate'])

app.controller('animateController', function($scope) {
    $scope.showRectangle = false;
    $scope.extraClass = false;
});