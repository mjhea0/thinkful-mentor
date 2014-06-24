# Defining a Controller

## Method 1

```javascript
var app = angular.module('app', []);

var MainController = function($scope) {
    $scope.val = "test123"
}
```

Issue: Polutes global name space. DO NOT USE.

## Method 2

```javascript
var app = angular.module('app', []);

app.controller('MainController', function($scope) {
  $scope.val = "test123"
})

Issue: Not modular. Okay for small apps. Will suffice for the Thinkful course.
```

## Method 3

var app = angular.module('app', ['controllers']);

```javascript
angular.module('controllers', []).controller('MainController', function($scope) {
    $scope.val = "test123"
})
```

Issue: Meant for product apps. Each controller should be in a separata JS file. It's a bit verbose for the Thinkful course.