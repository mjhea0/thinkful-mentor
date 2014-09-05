describe("My First Test", function(){

    it("should be true", function(){
        expect(true).toBe(true);
    });
});


describe('Routes!', function(){
  beforeEach(module("CountriesCapitalsApp"));

  it('should load home template', function(){
    inject(function($route, $rootScope, $location, $httpBackend){
      var route = $route.routes['/'];
      $httpBackend.whenGET(route.templateUrl).respond('...');

      $rootScope.$apply(function() {
        $location.path(route.originalPath);
      });

      expect($route.current.templateUrl).toBe("./home/home.html");
    });
  });

  it('should load countries template', function(){
    inject(function($route, $rootScope, $location, $httpBackend){
      var route = $route.routes['/countries'];
      $httpBackend.whenGET(route.templateUrl).respond('...');

      $rootScope.$apply(function() {
        $location.path(route.originalPath);
      });

      expect($route.current.templateUrl).toBe("./countries/countries.html");
    });
  });

});