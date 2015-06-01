angular.module('dataServices', [])


.factory('weatherData', ['apiFactory', function(apiFactory) {
	var weatherData = {};

	weatherData.getWeather = apiFactory.getWeather;

	return weatherData;

}])

.factory('locationData', ['locationFactory', function(locationFactory) {
	var locationData = {};

	locationData.yourLocation = locationFactory.getLocation();

	return locationData;
}])



.factory('locationFactory', ['$http','$q', function($http, $q){
	return {
		getLocation: function(){
			var deferred = $q.defer();

			window.navigator.geolocation.getCurrentPosition(function(pos){
				console.log(pos);
				$http.get('http://maps.googleapis.com/maps/api/geocode/json?latlng='+pos.coords.latitude+','+pos.coords.longitude+'&sensor=true')
				.success(function(data,status,headers,config){
					if(typeof data.status == 'object') {
						deferred.reject(data.status);
					} 
					else {
						deferred.resolve(data);
					}
				})
				.error(function(data, status, headers, config) {
					deferred.reject();
				});	

				
			});
			return deferred.promise;
		}
	};
}])

.factory('apiFactory', ['$http','$q',function($http, $q){

	var apiKey = '2e456563caa3d7dad1539f11bf756d5a/';
	var urlBase = 'https://api.forecast.io/forecast/' + apiKey;
	var request = {
		callback: 'JSON_CALLBACK',
		exclude: 'flags'
	};

	return {

		getWeather: function(lat,lon){
			var deferred = $q.defer();
			var url = urlBase + lat + ',' + lon;

			$http({
				method: 'JSONP',
				url: url,
				params:request,
				cache: true
			})

			.success(function(data, status, headers, config) {
				if(typeof data.status == 'object') {
					deferred.reject(data.status);
				} 
				else {
					deferred.resolve(data);
				}
			})

			.error(function(data, status, headers, config) {
				deferred.reject();
			});

			return deferred.promise;
		}
	};
}]);



