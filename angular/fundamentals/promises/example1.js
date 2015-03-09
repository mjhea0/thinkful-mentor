var app = angular.module('myApp', []).controller( 'myController', myController);

function myController( $q, $timeout) {


  function promiseOne() {
    var deferred = $q.defer();
    console.log("waiting for promiseOne to resolve...");
    $timeout(function() {
      deferred.resolve('promise one');
    }, 1000);
    return deferred.promise;
  }

  function promiseTwo() {
    var deferred = $q.defer();
    console.log("waiting for promiseTwo to resolve...");
    $timeout( function() {
      deferred.resolve( 'promise two');
    }, 2000);
    return deferred.promise;
  }

  function promiseThree() {
    var deferred = $q.defer();
    console.log("waiting for promiseThree to resolve...");
    $timeout( function() {
      deferred.resolve( 'promise three');
    }, 3000);
    return deferred.promise;
  }

  promiseOne().then(function(msg){
    console.log('received '+ msg);
    return promiseTwo();
  })
  .then(function(msg){
    console.log('received '+ msg);
    return promiseThree();
  })
  .then(function(msg){
    console.log('received '+ msg);
  });

}