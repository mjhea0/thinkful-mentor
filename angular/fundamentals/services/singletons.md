# Singletons

Angular Services are Singletons ...

## What's a Singletong?

Services are singletons, which is a design pattern that limits the instantiantion, by the `$injector`, of the class to only once per app. Thus, every area where you inject the service, it's using the same instance.

## Why should you use them?

Used for when an object needs to maintain a global state while also isolating the code from the global namespace.

## JavaScript Example

```
var mySingleton = function () {

    /*private variables and functions */

    var privateVariable = 'foo is private';

    function privateFunction() {
        alert(privateVariable);
    }

    /* public variables and functons */
    return {
        publicFunction: function() {
            privateFunction();
        },
        publicVariable: 'this is publicly accessible'
    }
}

var single = mySingleton(); // instantiates the class
single.publicFunction(); // alerts 'foo is private'
alert(single.publicVariable); // alerts 'this is publicly accessible'
```

### What's happening?

Here have private variables and functions by encapsulating variable and function declarations inside a closure, and exposing only those that we want to be publicly accessible.

Run this in your console. What happens?

## Angular Service (Factory) Example

Let's look at a quick example of a Factory.

```javascript
app.factory('foo', function() {
  var privateVariable = "This is private";
  function getPrivateVariable() {
    return privateVariable;
  }

  return {
    publicVariable: "This is public",
    getPrivateVariable: getPrivateVariable
  };
});
```

Now let's finish the module:

```javascript
var app = angular.module("myApp", []);

app.controller('myCtrl', function($scope, foo) {
  $scope.foo = foo;
});
```

So, we have this:

```javascript
var app = angular.module("myApp", []);

app.controller('myCtrl', function($scope, foo) {
  $scope.foo = foo;
});

app.factory('foo', function() {
  var privateVariable = "This is private";
  function getPrivateVariable() {
    return privateVariable;
  }

  return {
    publicVariable: "This is public",
    getPrivateVariable: getPrivateVariable
  };
});
```

Toss in some HTML:

```html
<!doctype html>
<html lang="en" ng-app='myApp'>
<head>
  <meta charset="UTF-8">
  <title>Angular Factory Example</title>
  <!-- styles -->
  <link href="http://netdna.bootstrapcdn.com/bootswatch/3.1.1/yeti/bootstrap.min.css" rel="stylesheet" media="screen">
  <style>
    .container {
      text-align: center;
      max-width: 400px;
      padding-top: 50px;
    }
  </style>
</head>
  <body>
    <div class="container">
      <div ng-controller="myCtrl">
        <h1>Angular Factory Example</h1>
        <br>
        <p>public: {{foo.publicVariable}}</p>
        <p>private: {{foo.getPrivateVariable()}}</p>
      </div>
    </div>
    <!-- scripts -->
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.16/angular.min.js" type="text/javascript"></script>
    <script src="singletons.js" type="text/javascript"></script>
  </body>
</html>
```

OUTPUT:

```
public: This is public

private: This is private
```
