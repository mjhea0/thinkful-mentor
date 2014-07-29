angular.module('CountriesCapitalsApp')

.controller('CountriesController', [
    '$scope',
    'CountryRepo',
    function($scope, CountryRepo) {
        // get all countries
        CountryRepo.getCountryList()
        .then(function(result) {
            // append to dom
            $scope.countries = result.geonames;
        });
    }
]);