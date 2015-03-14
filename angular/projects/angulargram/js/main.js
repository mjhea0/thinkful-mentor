angular.module('instagramApp', ['ngAnimate'])

  .controller('MainCtrl', function($scope, $http) {

    $scope.pictures = [];
    $scope.messageText = "";
    $scope.needTag = true;
    $scope.requiredFields = false;

    $scope.submit = function() {

      var url = "https://api.instagram.com/v1/tags/" + $scope.instaTag + "/media/recent";

      var request = {
          client_id: "cc46081f946241dab2ca8ddb7a7fa4f6",
          outputMode: 'json',
          showSourceText: '1',
          callback: "JSON_CALLBACK"
      };

      if ($scope.myForm.instaTag.$error.required) {
        $scope.requiredFields = true;
        document.getElementById("instaTag").focus();

      } else {
        $scope.requiredFields = false;
        $scope.needTag = true;
        setTimeout(function(){},5000);
        $scope.messageText = 'Searching Instagram for photos tagged with "' + $scope.instaTag + '"';
        $http({
          method: 'JSONP',
          url: url,
          params: request
        }).
        success(function(result) {
          if (result.data === undefined) {
            $scope.messageText = 'We found no results for "' + $scope.instaTag + '"';
            $scope.instaTag = "";
          } else {
            $scope.needTag = false;
            $scope.pictures = result.data;
            $scope.messageText = 'We found ' + String($scope.pictures.length) + ' results for "' + $scope.instaTag + '"';
            $scope.instaTag = "";
          }
            document.getElementById("instaTag").focus();
          }).
          error(function() {
            alert('error');
          });
      }

    };

  });

