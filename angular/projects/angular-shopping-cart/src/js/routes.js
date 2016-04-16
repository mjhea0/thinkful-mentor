app.config(function($routeProvider){
  $routeProvider
    .when('/', {
      templateUrl: 'partials/items.html',
      controller: 'mainController'
    })
    .when('/checkout', {
      templateUrl: 'partials/checkout.html',
      controller: 'cartController'
    })
    .otherwise({
      redirectTo: '/'
    });
});