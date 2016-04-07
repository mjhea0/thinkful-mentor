app.controller('detailsCtrl', function($scope, mealDataService) {

  $scope.mealCount = 1;

  // grab the current meal count
  var getMealCount = function(){
    var meals = mealDataService.getMeals();
    if(typeof meals != "undefined" && meals !== null && meals.length > 0) {
      $scope.mealCount = meals.length + 1;
    }
  };
  getMealCount();

  // clear form
  var cancelForm = function(){
    $scope.price = '';
    $scope.tax = '';
    $scope.tip = '';
  };

  // add new meal
  $scope.addTransaction = function() {

    $scope.mealCount++;

    var price = parseFloat($scope.price);
    var tax = parseFloat($scope.tax);
    var tip = parseFloat($scope.tip);

    var currentSubtotal = price + (price * (tax / 100));
    var currentTip = currentSubtotal * (tip / 100);
    var currentTotal = currentSubtotal + currentTip;

    // send current meal totals to the service
    var meal = {
      subtotal: currentSubtotal,
      tip: currentTip,
      total: currentTotal
    };
    mealDataService.addMeal(meal);

    // clear form
    cancelForm();

  };

});


app.controller('chargesCtrl', function($scope, mealDataService) {

  // get meals
  var getMeals = function(){
    var meals = mealDataService.getMeals();
    $scope.meals = meals;
  };
  getMeals();

  $scope.mealCount = $scope.meals.length;

  $scope.back = function(){
    if ($scope.mealCount > 1){
      $scope.mealCount--;
    }
  };

  $scope.forward = function(){
    if ($scope.mealCount < $scope.meals.length){
      $scope.mealCount++;
    }
  };

});

app.controller('earningsCtrl', function($scope, mealDataService) {
  $scope.tipTotal = mealDataService.getCumulativeData().tipTotal;
  $scope.mealCount = mealDataService.getCumulativeData().mealCount;
  $scope.tipAvg = mealDataService.getCumulativeData().tipAvg;
});


app.controller('resetCtrl', function($scope, $location, mealDataService) {
  // reset ALL totals
  $scope.resetAll = function(){
    mealDataService.resetAll();
    $location.path('/details');
  };
});