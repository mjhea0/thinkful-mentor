# Angular Services <> Singletons

Let's quickly prove that Angular services are singletons.

## Instantiate a new service

1. Start by adding this empty service to a module:

    ```javascript
    var app = angular.module('myApp', [])

    app.service('foo', function() {
      console.log(this)
    });
    ```

2. Then inject this service into a controller:

    ```javascript
    app.controller('myController', function(foo, $scope) {
      // empty
    });
    ```

3. Updated your HTML:

    ```html
    <!doctype html>
    <html lang="en" ng-app='myApp'>
    <head>
      <meta charset="UTF-8">
      <title>Angular Services</title>
    </head>
      <body>
        <div ng-controller="myController">
          <h1>Empty</h1>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.16/angular.min.js" type="text/javascript"></script>
        <script src="main.js" type="text/javascript"></script>
      </body>
    </html>
    ```

3. Open the page in either Chrome or Firefox and then open the console. Notice the `c {}`. This is a constructor object that is returned by [constructor function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function). This tells us that a services instantiate a constructor function, which is given a new scope. What's a constructor function? In JavaScript it's equivalent to calling a function with `new`. For more info check the link above.

## Add a Controller

1. Add a new controller and inject the service again:

    ```javascript
    app.controller('secondController', function(foo) {
        // empty
    });
    ```

2. Update your HTML by adding:

    ```html
    <div ng-controller="secondController">
      <h1>Empty</h1>
    </div>
    ```
3. Refresh your browser.

## What's happening?

There should just be one `c {}` in the console. No matter how many times you inject this service, there is only one instance - thus the service is a singleton.
