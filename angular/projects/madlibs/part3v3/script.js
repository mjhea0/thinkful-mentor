// Code goes here

angular.module('myApp', ['ngMessages'])
.controller('myCtrl', ['$scope', function ($scope) {
  $scope.submitMe = function () {
  	if ($scope.myForm.$submitted && $scope.myForm.$valid) {
  		console.log("Form is valid");
  		console.log("DATA: \n" + $scope.data);
    	console.log("myForm: \n" + $scope.myForm);
  	} else {
  		console.log("The Form is NOT valid.");
  		// $scope.myForm.$submitted = false;
  	}
  };
}]);