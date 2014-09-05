(function(){

  'use strict';

  angular.module('myEditableApp', [])
    .directive('makeEditable', function(){
        return {
          restrict: 'A',
          scope: true,
          transclude: true,
          templateUrl: 'make-editable.html',
          link: function($scope, element, attr){
            $scope.editingStatus = false;
            $scope.buttonText = 'edit me!';
            $scope.toggleEdit = function(){
              if($scope.editingStatus == false){
                $scope.editingStatus = true;
                $scope.buttonText = 'save me!';
              } else {
                $scope.editingStatus = false;
                $scope.buttonText = 'edit me!';
              }
            };
          }
        };
  });

}());