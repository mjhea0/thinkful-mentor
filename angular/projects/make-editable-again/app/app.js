var app = angular.module('editableApp', [])

app.directive('makeEditable', function(){
    return {
        restrict: 'E',
        scope: true,
        transclude: true,
        templateUrl: 'make-editable.html',
        link: function($scope, element, attr){
          $scope.editingStatus = false;
          $scope.buttonText = 'edit!';
          $scope.toggleEdit = function(){
            if($scope.editingStatus == false){
              $scope.editingStatus = true;
              $scope.buttonText = 'save!';
            } else {
              $scope.editingStatus = false;
              $scope.buttonText = 'edit!';
            }
          };
        }
    };
});