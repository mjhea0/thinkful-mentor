var app = angular.module('instaApp', ['ngAnimate'])

app.controller('instaController', function($scope, $http) {
    $scope.submitted = false
    $scope.message = null
    $scope.submit = function() {
        $scope.submitted = true;  // using HTML5 form validation
        var tag = $scope.instaData.tag;
        console.log("you searched for: " + tag)
        getImages(tag);
    };

    // search instagram
    function getImages(tag) {
        // api config
        var base = "https://api.instagram.com/v1";
        var clientId = '890e785cf1ea43f2997d57cc47f91bb8';
        // request url
        var request = '/tags/' + tag + '/media/recent';
        var url = base + request;
        // parameters
        var config = {
            'params': {'client_id': clientId, 'callback': 'JSON_CALLBACK', 'count': 15,}
        };
        $http.jsonp(url, config).success(function (results) {
            if (results.meta.code == 200) {
                if (results.data.length > 0) {
                    $scope.images = results.data;
                    $scope.message = "Found " +results.data.length+ " results tagged with '" +tag+ "' ..."
                } else {
                    $scope.message = "Sorry. No results were found."
                }
            } else {
                $scope.message = "Oops! Error: '" +result.meta.error_type+"'."
            }
        }).error(function() {
            $scope.message = "Oops! Error."
        });
    }

    $scope.reset = function() {
        console.log("test")
        $scope.submitted = false
        $scope.message = null
        $scope.instaData = {}
        $scope.images = {}
    }

});

