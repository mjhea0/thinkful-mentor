angular.module('HelloModule', [])
.factory('uppercaseService', function() {
        return function() {
            return 'hello';
        }
    })
.factory('helloService', function(uppercaseService) {
    return function() {
        return uppercaseService('hello');
    }
});