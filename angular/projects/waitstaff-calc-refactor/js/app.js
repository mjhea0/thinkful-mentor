angular.module('waitStaffCalc', [] )
.controller('calcController', function($scope) {

  function initMealDetails() {
    $scope.mealDetails = {
      base: 0,
      taxRate: 0,
      tipPercentage: 0
    };
  }

  function initMealTotals() {
    $scope.totals = {
      subtotal: 0,
      tip: 0,
      total: 0,
      tipTotal: 0,
      averageTip: 0,
      count: 0
    };
  }

  initMealDetails();
  initMealTotals();

  $scope.submit = function() {
    // update meal details
    $scope.mealDetails.taxRate = $scope.mealDetails.taxRate * 0.01;
    // calculate charges
    $scope.totals.subtotal = ($scope.mealDetails.base * $scope.mealDetails.taxRate) + $scope.mealDetails.base;
    $scope.totals.tip = ($scope.mealDetails.tipPercentage / 100) * $scope.totals.subtotal;
    $scope.totals.total = $scope.totals.tip + $scope.totals.subtotal;
    // calculate total earnings
    $scope.totals.count++;
    $scope.totals.tipTotal += $scope.totals.tip;
    $scope.totals.averageTip = $scope.totals.tipTotal / $scope.totals.count;
    // reset meal details
    initMealDetails();
  };


  $scope.reset = function() {
    initMealDetails();
    initMealTotals();
  };

  $scope.cancel = function() {
    initMealDetails();
  };

});
