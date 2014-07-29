angular.module('DataServices', [])

.factory('CountryRepo', [
    '$http',
    '$route',
    function($http, $route) {

        return ({
            getCountryList: getCountryList,
            getCountry: getCountry,
            getNeighborList: getNeighborList,
            getCapitalDetails: getCapitalDetails
        });
        // all countries
        function getCountryList() {
            var url = "http://api.geonames.org/countryInfoJSON?username=mjhea0";
            var request = $http.get(url, { cache: true });
            return (request.then(handleSuccess, handleError));
        };
        // idividual countries
        function getCountry() {
            var url = "http://api.geonames.org/countryInfoJSON?username=mjhea0&country=" + $route.current.params.countryCode;
            var request = $http.get(url);
            return (request.then(handleSuccess, handleError));
        };
        // neighbors
        function getNeighborList() {
            var url = "http://api.geonames.org/neighboursJSON?username=mjhea0&country=" + $route.current.params.countryCode;
            var request = $http.get(url);
            return (request.then(handleSuccess, handleError));
        };
        // capital
        function getCapitalDetails() {
            var url = "http://api.geonames.org/searchJSON?formatted=true&username=mjhea0&q=capital&&style=full&country=" + $route.current.params.countryCode;
            var request = $http.get(url);
            return (request.then(handleSuccess, handleError));
        };

        // handle the error
        function handleError(response) {
            // throw error
            throw(response.data.message);
        }

        // handle success
        function handleSuccess(response) {
            // return response
            return (response.data);
        }
    }
]);