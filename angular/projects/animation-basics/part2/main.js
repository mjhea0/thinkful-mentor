var app = angular.module('animateApp', ['ngAnimate'])

app.controller('animateController', function($scope) {
    $scope.groceries = [
        'Milk', 'Eggs', 'Bacon', 'Coffee', 'Wine', 'Spinach', 'Apples', 'Beans', 'Flour', 'Pork', 'Onion', 'Jam',
        'Paper Towels', 'Ice Cream', 'Blueberries', 'Cookies', 'Pie', 'Lettuce', 'Green Onion', 'Apple Pie', 'Tea', 'Beef'
    ];
});