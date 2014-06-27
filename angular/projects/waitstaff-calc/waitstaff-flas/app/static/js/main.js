$(function() {
  // test to ensure jQuery is working
  console.log("whee!")
});


// start of angular code

var app = angular.module("earningsApp", []);

app.controller('earningsController', function($scope, $http) {

  var getData = function() {
    $http.get('/api/v1/earnings')
    .success(function(items) {
      console.log(items)
      $scope.items = items;
    })
    .error(function(items) {
      console.log('Error: ' + items);
    });
  };

  var init = function() {

    // totals
    $scope.mealData = {};
    $scope.charges = {};

    // total values
    $scope.charges.subtotal = 0;
    $scope.charges.tip = 0;
    $scope.charges.total = 0;
    $scope.submitted = false;
  };

  // call init(), getData() functions
  init(); 
  getData();

  // compute totals
  var compute = function() {

    // total per customer
    $scope.charges.subtotal = ($scope.mealData.mealPrice * (1 + $scope.mealData.taxRate/100));
    $scope.charges.tip = $scope.charges.subtotal * $scope.mealData.tipRate/100;
    $scope.charges.total = $scope.charges.subtotal + $scope.charges.tip;

    // post request
    $http.post(
      '/api/v1/earnings',
      JSON.stringify($scope.mealData),
      {'Content-Type': 'application/json'}
    )
    .success(function(data) {
      console.log(data)
      getData();
    });
  };

  // validate data
  $scope.validate = function() {
    if($scope.mealForm.$valid) {
      compute();  // run form validation before computing totals
    }
  }

  // clear input fields
  $scope.clear = function() {
    $scope.mealData = {};
    $scope.charges = {"subtotal":0,"tip":0,"total":0}
    $scope.submitted = false;
  }

});