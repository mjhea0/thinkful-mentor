var app = angular.module('app', []);

app.controller('MainController', function($scope) {
    $scope.first = [1,2,3,4,5,6,7,8,9]
    $scope.second = [{name:"mike",age:23},{name:"andy",age:34},{name:"reid",age:45},{name:"reid",age:45}]
    $scope.third = {name: "mike", age:35, title:"Mr."}
    $scope.fourth = [1,2,3,4,5,5,6,7,8,9]
})