describe("SettingsModule", function() {
  beforeEach(module("SettingsModule"));

  describe("/settings route", function() {
    it('should load the page and controller', inject(function($location, $rootScope, $httpBackend, $rootElement, $compile) {
      var view = $compile('<div ng-view></div>')($rootScope);
      $rootElement.append(view);
      $httpBackend.whenGET('settings.html').respond('...');
      $httpBackend.whenGET('/api/current-user').respond({});
      $rootScope.$apply(function() {
        $location.path('/settings');
      });
      $httpBackend.flush();
      expect($rootScope.page).toBe("settings");
    }));
  });
});