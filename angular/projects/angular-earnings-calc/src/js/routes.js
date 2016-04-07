app.config(['$routeProvider', function($routeProvider) {
  $routeProvider
    .when('/details', {
      templateUrl: 'partials/details.html',
      controller:'detailsCtrl'
    })
    .when('/charges', {
      templateUrl: 'partials/charges.html',
      controller:'chargesCtrl'

    })
    .when('/earnings', {
      templateUrl: 'partials/earnings.html',
      controller:'earningsCtrl'
    })
    .otherwise({
      redirectTo: '/details'
    });
}]);