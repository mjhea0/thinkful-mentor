describe('countriesController', function () {

  var controller = null;
  $scope = null;

  beforeEach(function () {
    module('ccApp');
  });

  beforeEach(inject(function ($controller, $rootScope) {
    $scope = $rootScope.$new();
    controller = $controller('countriesController', {
      $scope: $scope
    });
  }));

  it('initial predicate value should equal country name', function () {
    expect($scope.predicate).toEqual("countryName");
  });

});