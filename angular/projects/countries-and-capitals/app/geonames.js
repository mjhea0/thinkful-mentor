angular.module('cncApp').factory('geonamesFactory',
    ['$http', '$q',
    function($http, $q){
        var username = "mjhea0";
        var PrimaryUrl = "http://api.geonames.org/";
    return {
        getCountriesInfo: function(){
            var d = $q.defer();
            var url = PrimaryUrl + "countryInfoJSON";
            var request = {
                callback: 'JSON_CALLBACK',
                username: username
            };
            $http({
                method: 'JSONP',
                url: url,
                params: request,
                cache: true
            }).success(function(data, status, headers, config) {
                if(typeof data.status == 'object') {
                    alert("Encountered and error requesting country data: \r\n'" +
                        data.status.message + "'");
                    d.reject(data.status);
                } else {
                    //Creating a countries index value pair: countryCode,
                    //index of the country in the countries array.
                    data.index = {};
                    for (i=0; i<data.geonames.length; i++) {
                        data.index[data.geonames[i].countryCode]=i;
                    }
                    //Return both the index object and countries array:
                    d.resolve(data);
                }
            }).error(function(data, status, headers, config) {
                alert(status + " error attempting to access geonames.org.");
                d.reject();
            });
            return d.promise;
        },
        getNeighbors: function(countryCode){
            var d = $q.defer();
            var url = PrimaryUrl + "neighboursJSON";
            var request = {
                callback: 'JSON_CALLBACK',
                country: countryCode,
                username: username
            };
            $http({
                method: 'JSONP',
                url: url,
                params: request,
                cache: true
            }).success(function(data, status, headers, config) {
                d.resolve(data);
            }).error(function(data, status, headers, config) {
                alert(status + " error attempting to access geonames.org.");
                d.reject();
            });
            return d.promise;
        },
        getCapitalInfo: function(countryCode) {
            var d = $q.defer();
            var url = PrimaryUrl + "searchJSON";
            var request = {
                callback: 'JSON_CALLBACK',
                q: "capital",
                formatted: true,
                country: countryCode,
                maxRows: 1,
                username: username
            };
            $http({
                method: 'JSONP',
                url: url,
                params: request,
                cache: true
            }).success(function(data, status, headers, config){
                d.resolve(data.geonames[0]);
            }).error(function(data, status, headers, config){
                alert(status + " error attempting to access geonames.org.");
                d.reject();
            });
            return d.promise;
        }
    };
}]);