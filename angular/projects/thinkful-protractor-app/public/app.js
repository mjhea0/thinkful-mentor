angular.module("UrlApp", ['ngAnimate', 'ngRoute', 'ngMessages'])

  .constant('API_URL', '/api')

  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
      redirectTo : '/urls'
    });
    $routeProvider.when('/error', {
      template : 'Error Page Not Found...'
    });
    $routeProvider.when('/urls', {
      controller: 'ListCtrl as listCtrl',
      templateUrl : './templates/list.html',
      reloadOnSearch : false
    });
    $routeProvider.when('/new', {
      controller: 'FormCtrl as formCtrl',
      templateUrl : './templates/form.html',
      resolve : {
        entry : function() {
          return null;
        }
      }
    });
    $routeProvider.when('/edit/:id', {
      controller: 'FormCtrl as formCtrl',
      templateUrl : './templates/form.html',
      resolve : {
        entry : ['$http', 'API_URL', '$route', '$q', function($http, API_URL, $route, $q) {
          var defer = $q.defer();
          $http.get(API_URL + '/urls/' + $route.current.params.id)
            .success(function(url) {
              defer.resolve(url);
            })
            .error(function() {
              defer.reject();
            })
          return defer.promise;
        }]
      }
    });
    $routeProvider.otherwise({
      redirectTo : '/urls'
    });
  }])

  .run(['$rootScope', '$location', function($rootScope, $location) {
    $rootScope.$on('$routeChangeError', function() {
      $location.path('/error');
    })
  }])

  .controller('SearchCtrl', ['$location', '$scope', '$routeParams', '$rootScope', function($location, $scope, $routeParams, $rootScope) {
    var ctrl = this;

    $scope.$on('$routeChangeSuccess', function() {
      ctrl.q = $routeParams.q;
    });

    $scope.$watch(
      function() {
        return ctrl.q;
      },
      function(q) {
        if(q && q.length) {
          $location.path('/urls').search({ q : q });
          $rootScope.q = q;
        }
      });
  }])

  .controller('ListCtrl', ['API_URL', '$http', '$window', function(API_URL, $http, $window) {
    var ctrl = this;
    var baseURL = $window.location.toString().match(/(https?:\/\/.+?)\//)[1] + API_URL;

    $http.get(API_URL + '/urls').success(function(urls) {
      ctrl.results = _.map(urls, function(url) {
        url.actual_url = baseURL + url.shortened_url;
        return url;
      });
    });

    ctrl.destroy = function(entry) {
      var index = ctrl.results.indexOf(entry);
      if(index >= 0) {
        ctrl.results.splice(index, 1);
        $http.delete(API_URL + '/urls/' + entry.id);
      }
    }
  }])

  .controller('FormCtrl', ['$http', 'API_URL', '$location', 'entry', function($http, API_URL, $location, entry) {
    var edit, ctrl = this;
    if(entry) {
      ctrl.form = entry;
      edit = ctrl.edit = true;
    }

    this.submit = function(form, valid) {
      if(!valid) return;

      ctrl.loading = true;

      if(edit) {
        $http.put(API_URL + '/urls/' + entry.id, form).success(ready);
      } else {
        $http.post(API_URL + '/urls', form).success(ready);
      }

      function ready(data) {
        ctrl.results = data;
        ctrl.loading = true;
        $location.path('/urls').search({item : url.id});
      }
    };
  }])
