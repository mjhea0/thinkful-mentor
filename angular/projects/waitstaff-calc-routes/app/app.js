angular.module('ngWaitstaffApp', ['ngRoute'])

// globals
.constant('DEFAULT_TAX_RATE', 9.50)
.value('earnings', [])

.config(function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl : 'partials/home.html'
    }).when('/new-meal', {
        templateUrl : 'partials/newmeal.html',
        controller : 'inputController'
    }).when('/earnings', {
        templateUrl : 'partials/earnings.html',
        controller : 'EarningsCtrl'
    })
    .otherwise({ redirectTo : '/' });
})

.controller('inputController', function($scope, earnings, DEFAULT_TAX_RATE) {
    $scope.input = {};
    $scope.subtotal = $scope.tip = $scope.total = null;
    $scope.init = function() {
        $scope.input.meal_price = null;
        $scope.input.tip_percentage = null;
        $scope.input.tax_rate = DEFAULT_TAX_RATE;
        $scope.submitted = false;
        $('#meal_price').focus();
    };

    $scope.submit = function() {
        calculateMeal($scope.input);
        calculateEarnings($scope.input);
        $scope.cancel();
    };

    function calculateMeal(input) {
        $scope.subtotal = input.meal_price + (input.meal_price * input.tax_rate/100);
        $scope.tip = input.meal_price * input.tip_percentage/100;
        $scope.total = $scope.subtotal + $scope.tip;
    }

    function calculateEarnings(input) {
        earnings.push({'meal_price':input.meal_price, 'tax_rate':input.tax_rate, 'tip_percentage':input.tip_percentage});
    }

    $scope.cancel = function() {
        $scope.init();
        $scope.mealForm.$setPristine();
    };

    $scope.$on('resetCtrl', function(event, input) {
        $scope.cancel();
    });
    $scope.init();

})

.controller('EarningsCtrl', function($scope, earnings) {
    $scope.tip_total = $scope.meal_count = $scope.average_tip = 0;
    for (var meal in earnings) {
        $scope.tip_total += earnings[meal].meal_price * earnings[meal].tip_percentage/100;
        $scope.meal_count += 1;
        $scope.average_tip = $scope.tip_total / $scope.meal_count;
    }

    $scope.resetCalc = function() {
        earnings.length = 0;
        $scope.tip_total = $scope.meal_count = $scope.average_tip = 0;
    };
});
