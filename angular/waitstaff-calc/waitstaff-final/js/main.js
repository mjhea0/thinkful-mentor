var waitstaffApp = angular.module("waitstaffApp", []);

waitstaffApp.controller('inputController', function($scope, $rootScope) {
    $scope.submit = function() {
        $scope.submitted = true;
        $rootScope.$broadcast("calculate", $scope.input);
        $scope.submitted = false;
        resetForm();
    }
    $scope.$on("reset", function() {
        resetForm();
    });

    $scope.cancel = function() {
        resetForm();
    };

    function resetForm() {
        $scope.input = {
            meal_price:0,
            tax_rate:0,
            tip_percent:0
        };
    }
})
.controller("customerController", function($scope ,$rootScope) {
    $scope.customer={
        subtotal:0,
        tip:0,
        total:0
    }
    $scope.$on("calculate", function(event, data) {
        resetCustomer();
        $scope.customer.subtotal = data.meal_price *(100+data.tax_rate)/100;
        $scope.customer.tip = data.meal_price *(data.tip_percent)/100;
        $scope.customer.total = $scope.customer.subtotal + $scope.customer.tip;
        $rootScope.$broadcast("tip_result",$scope.customer);
    });
    $scope.$on("reset", function() {
        resetCustomer();
    });

    function resetCustomer() {
        $scope.customer= {
            subtotal:0.00,
            tip:0.00,
            total:0.00
        }
    }
})
.controller("earnController", function($scope) {
    $scope.earn= {
        tip_total:0.00,
        meal_count:0,
        average_tip:0.00
    }
    $scope.$on("tip_result", function(event, data) {
        $scope.earn.tip_total += data.tip;
        $scope.earn.meal_count += 1;
        $scope.earn.average_tip += $scope.earn.tip_total / $scope.earn.meal_count;
    });
    $scope.$on("reset", function() {
        $scope.earn= {
        tip_total:0,
        meal_count:0,
        average_tip:0
    }
    });
})
.controller("resetController", function($scope, $rootScope) {
    $scope.reset=function() {
        console.log("reset");
        $rootScope.$broadcast("reset");
    };
});
