# Angular Services === Singletons

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
    app.controller('firstCtrl', function(foo) {
      // empty
    });
    ```

3. Update your HTML:

    ```html
    <!doctype html>
    <html lang="en" ng-app='myApp'>
    <head>
      <meta charset="UTF-8">
      <title>Angular Services</title>
    </head>
      <body>
        <div ng-controller="firstCtrl">
          <h1>Empty</h1>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.16/angular.min.js" type="text/javascript"></script>
        <script src="main.js" type="text/javascript"></script>
      </body>
    </html>
    ```

3. Open the page in either Chrome or Firefox and then open the console. Notice the `c {}`. This is a constructor object that is returned by a [constructor function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function). This tells us that services instantiate a constructor function, which is given a new scope. What's a constructor function? In JavaScript it's equivalent to calling a function with `new`. For more info check the link above.

## Sanity Check

1. Add a new controller and inject the service again:

    ```javascript
    app.controller('secondCtrl', function(foo) {
      // empty
    });
    ```

2. Update your HTML by adding:

    ```html
    <div ng-controller="secondCtrl">
      <h1>Second Controller</h1>
    </div>
    ```
3. Refresh your browser.

### What's happening?

There should just be one `c {}` in the console. No matter how many times you inject this service, there is only one instance - thus the service is a singleton.

## Equality Check

1. Update the `firstCtrl`:

    ```javascript
    app.controller('firstCtrl', function(foo) {
      var a = foo;
      var b = foo;
      console.log("Are they equal?", a===b)
    });
    ```

2. Refresh your browser. You should see: *Are they equal? true* in the console.

## How about a Factory?

1. Add a new Factory service:

    ```javascript
    app.factory('bar', function() {
      console.log(this)
    });

    app.controller('thirdCtrl', function(bar) {
      // empty
    });

    app.controller('fourthCtrl', function(bar) {
      // empty
    });
    ```

2. Update the HTML:

    ```html
    <div ng-controller="thirdCtrl">
      <h1>Third Controller</h1>
    </div>
    <div ng-controller="fourthCtrl">
      <h1>Fourth Controller</h1>
    </div>
    ```

3. Refresh! What do you see? Again, you should see another constuctor function, `Object {$get: function}`. And again, since there is only one, even though we injected it twice, a Factory is also a singleton.

## Conclusion

Services are singletons.
