app = angular.module('waitstaff', [])
app.controller('waitstaffController', function($scope) {

  var init = function() {

    // totals
    $scope.mealData = {};
    $scope.charges = {};
    $scope.earnings = {};

    // total values
    $scope.charges.subtotal = 0;
    $scope.charges.tip = 0;
    $scope.charges.total = 0;
    $scope.earnings.tip_total = 0;
    $scope.earnings.meal_count = 0;
    $scope.earnings.avg_tip = 0;
    $scope.submitted = false;
  };

  // call init() function
  init(); 

  // compute totals
  var compute = function() {

    // total per customer
    $scope.charges.subtotal = ($scope.mealData.mealPrice * (1 + $scope.mealData.taxRate/100));
    $scope.charges.tip = $scope.charges.subtotal * $scope.mealData.tipRate/100;
    $scope.charges.total = $scope.charges.subtotal + $scope.charges.tip;
  
    // totals
    $scope.earnings.tip_total += $scope.charges.tip;
    $scope.earnings.meal_count++;  // no for loop - ha
    $scope.earnings.avg_tip = $scope.earnings.tip_total / $scope.earnings.meal_count;
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

  // reset total earnings
  $scope.reset = function() {
    $scope.earnings = {};
    $scope.earnings.tip_total = 0;
    $scope.earnings.meal_count = 0;
    $scope.earnings.avg_tip = 0;
    // init(); // may be better to just call init() here instead
  }

});