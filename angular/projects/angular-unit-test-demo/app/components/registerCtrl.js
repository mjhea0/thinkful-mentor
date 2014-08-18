angular.module('RegisterModule', ["UsernameModule"])
.controller('RegisterCtrl', function(usernameAvailable, $scope) {
        $scope.submit = function(data) {
            //send data to the API...
        };
});