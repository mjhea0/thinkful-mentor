describe('cncApp', function() {
    var $rootScope, $state, $injector

    beforeEach(function() {
        module('cncApp');
        inject(function(_$rootScope_, _$state_, _$injector_, $templateCache) {
            $rootScope = _$rootScope_;
            $state = _$state_;
            $injector = _$injector_;
            $templateCache.put('partials/home/home.html', '');
            $templateCache.put('partials/countries/countries.html', '');
        });
    });

    //Spec for the constant block:
    it('has a version', function() {
        inject(function(VERSION) {
            expect(VERSION).not.toBeUndefined();
        });
    });

    //Spec for run block.
    it('should have an initial state of "home"', function() {
        $rootScope.$digest();
        expect($state.current.name).toBe('home');
    });

    //Specs for config block is corretly using ui-router:
    it('should have the routings defined', function() {
        expect($state.href('home')).toBe('#/');
        expect($state.href('countries')).toBe('#/countries');
        expect($state.href('countryDetail', { countryCode: 'ZZ'})).toBe('#/countries/ZZ');
        //Check otherwise routing behavior:
        expect($state.href('notDefined')).toBeNull;
        inject(function($location) {
            $location.path('/notDefined');
            $rootScope.$digest();
            expect($location.path()).toBe('/');
        });
    });

    //Spec for appCtrl controller:
    describe('appCtrl', function() {
        beforeEach(inject(function($controller, $rootScope) {
            $document = angular.element(document);
            $document.find('body').append('<div id="BrowseCountries"></div>');
            $scope = $rootScope.$new();
            $controller('appCtrl', {
                $scope: $scope,
                cncData: {
                        version: -1
                    }
            });
        }));

        afterEach(function() {
            document.getElementById("BrowseCountries").remove();
        });

        it('should instantiate "cncCtrl" to preload countries data', function() {
            expect($scope.version).toBe(-1);
        });
    });
});

//Spec for cncData service:
describe('cncData', function() {
    beforeEach(function() {
        module('cncApp');
        module(function($provide) {
            $provide.value('geonamesFactory', {
                getCountriesInfo: function() {return 'country'},
                getCapitalInfo: function(countryCode) {},
                getNeighbors: function(countryCode) {}
            });
        });
    });
    it('should return "Data" when called', function() {
        inject(function(cncData) {
            expect(cncData.countries).toEqual('country');
            expect(cncData.version).not.toBeUndefined;
        })
    });
});
