var app = angular.module('ngMadLibs', ['ngAnimate'])

app.constant('VERSION', "4")
app.run(function(VERSION, $rootScope) {
    $rootScope.version = VERSION;
})

app.controller('madLibsController',function($scope){

    $scope.data = {};

    $scope.gender = {
        pronoun: 'she',
        poss: 'her'
    };

    $scope.hideForm = false;

    $scope.submit = function(){
        $scope.hideForm = true;
    }

    $scope.reset = function(){
        $scope.data = {};
        $scope.hideForm = false;
        $scope.submitted = false;
    }

});