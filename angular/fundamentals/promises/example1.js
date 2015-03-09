var app = angular.module('myApp', []).controller( 'myController', MyCtrl);
function myController( $q, $timeout) {
  function f() {
    var deferred = $q.defer();
    $timeout( function() {
        deferred.resolve( 'f');
    }, 100);
    return deferred.promise;
  }
  function g() {
    var deferred = $q.defer();
    $timeout( function() {
        deferred.resolve( 'g');
    }, 500);
    return deferred.promise;
  }
  function h() {
    var deferred = $q.defer();
    $timeout( function() {
        deferred.resolve( 'h');
    }, 500);
    return deferred.promise;
  }
    f()
    .then( function( msg){
        console.log( 'received '+ msg);
        return g()})
    .then( function( msg){
        console.log( 'received '+ msg);
        return h()})
    .then( function( msg){
        console.log( 'received '+ msg);
    }, function() {
        console.log( 'error');
    });
}