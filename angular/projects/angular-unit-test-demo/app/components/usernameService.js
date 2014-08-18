angular.module('UsernameModule', [])
    .factory('usernameAvailable', function($http) {
        return function(username) {
            return $http.get('/api/username-available/' + username);
        }
    });