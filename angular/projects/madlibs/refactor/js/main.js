angular.module('madlibsRefactor', [])
  .controller('indexController', function($scope) {

    function init() {
      // initalize the scope variable
      $scope.content = {};
      // show form, hide passage
      $scope.form = true;
      $scope.passage = false;
    }

    // fire init on page load
    init();

    // handle form submission -> hide form, show passage
    $scope.submit = function() {
      $scope.form = false;
      $scope.passage = true;
    };

    // re-fire init, clearing everything
    $scope.reset = function(){
      init();
    };

  });

