$(function() {
  console.log('ready!');
});

angular.module('ngMadlibs', [])
  .controller('madlibsController', function($scope) {
    'use strict';
    $scope.submitForm = function() {
      // check to make sure the form is valid
      if ($scope.madForm.$valid) {
        if ($scope.madForm.gender.$modelValue === "Male") {
          $('#reset-btn').show()
          $('#male-text').show()
          $('#female-text').hide()
        } else if ($scope.madForm.gender.$modelValue === "Female") {
          $('#reset-btn').show()
          $('#female-text').show()
          $('#male-text').hide()
        }
      }
    }
    $scope.reset = function() {
      $scope.formData = {};
      $('#female-text').hide()
      $('#male-text').hide()
      $scope.madForm.$setPristine();
      $('#reset-btn').hide()
    }
  });


