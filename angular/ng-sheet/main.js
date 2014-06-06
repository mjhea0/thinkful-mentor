app = angular.module('supportApp', [])
app.controller('supportAppController', function($scope, $http) {

  var init = function() {
    $scope.head = {'name': "Name", 'issue': "Issue"};
    $scope.sort = {column: 'name', descending: false};
    $scope.supportData = {};
    $http.get('main.json')
      .then(function(res){
        $scope.arrayData = res.data;                
      });
    $scope.submitted = false;
  };

  // call init() function
  init(); 

  // validate data
  $scope.validate = function() {
    if($scope.supportForm.$valid) {
      compute();  // run form validation before computing totals
    }
  }

  var compute = function() {
    $scope.arrayData.push($scope.supportData);
    $scope.supportData = {};
    $scope.submitted = false;
  }

  // clear input fields
  $scope.clear = function() {
    $scope.supportData = {};
    $scope.submitted = false;
  }

    
  $scope.selectedCls = function(column) {
    return column == $scope.sort.column && 'sort-' + $scope.sort.descending;
  };
  
  $scope.changeSorting = function(column) {
    var sort = $scope.sort;
    if (sort.column == column) {
      sort.descending = !sort.descending;
    } else {
      sort.column = column;
      sort.descending = false;
    }
  };

});