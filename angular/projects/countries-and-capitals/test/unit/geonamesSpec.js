describe('geonames', function() {
  beforeEach(function(){
    module('cncApp');
        inject(function(_$rootScope_, _$state_, _$injector_, $templateCache) {
            $rootScope = _$rootScope_;
            $state = _$state_;
            $injector = _$injector_;
            $templateCache.put('partials/home/home.html', '');
        });
  });

  it('getCountriesInfo should query the geonames api for countries data',
    inject(function(geonamesFactory, $httpBackend, $q) {
      $httpBackend.when('JSONP', 'http://api.geonames.org/countryInfoJSON?callback=JSON_CALLBACK&username=sdavern')
        .respond({
          geonames: [{key:0}, {key:1}]
        });
      var countries
      $q.when(geonamesFactory.getCountriesInfo()).then(function(result){
        countries = result.geonames
      });
      $httpBackend.flush();
      expect(countries.length).toBe(2);
      $httpBackend.verifyNoOutstandingRequest();
  }));
});