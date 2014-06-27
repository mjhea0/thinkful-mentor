var app = angular.module('ngMadLibs', [])

app.constant('VERSION', "2.2") // good!
app.run(function(VERSION, $rootScope) {
    $rootScope.version = VERSION;
})

app.controller('madLibsController',function($scope){
    $scope.gender = {
        pronoun: 'she',
        poss: 'her'
    };

});