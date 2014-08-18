describe("RegisterModule", function() {
  beforeEach(module('RegisterModule'));
  describe('RegisterCtrl', function() {
    var ctrl, scope;
    beforeEach(inject(function($controller, $rootScope) {
      scope = $rootScope.$new();
      ctrl = $controller('RegisterCtrl', {
        $scope : scope,
        usernameAvailable : function() { return false; }
      });
    }));

    it('should submit the form data to the server', function() {
      scope.submit({
        username : "eric",
        age : 50
      });
    });
  });
});