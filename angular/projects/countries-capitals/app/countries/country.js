angular.module('CountriesCapitalsApp')

.controller('CountryController', [
    '$scope',
    'CountryRepo',
    function($scope, CountryRepo) {
        // get individual country
        CountryRepo.getCountry().then(function(result) {
            $scope.country = result.geonames[0];
        });
        // get neighboring countries
        CountryRepo.getNeighborList().then(function(result) {
            $scope.neighbors = result.geonames;
        });
        // get capitails
        CountryRepo.getCapitalDetails().then(function(result) {
            $scope.capitalPopulation = result.geonames[0].population;
        });
    }
]);