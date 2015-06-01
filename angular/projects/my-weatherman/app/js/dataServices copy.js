angular.module('dataServices', [])


.factory('weatherData', ['apiFactory', function(apiFactory) {
	var weatherData = {};

	weatherData.getWeather = apiFactory.getWeather;
	weatherData.getForecast = apiFactory.getForecast;

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

	var apiKey = 'bca2fe8e751fa329d36cc2408c27ebee';
	var urlBase = 'http://api.openweathermap.org/data/2.5/';
	var request = {
		callback: 'JSON_CALLBACK'
	};

	return {

		getWeather: function(lat,lon){
			var deferred = $q.defer();
			var url = urlBase + 'weather?lat=' + lat + '&lon=' + lon + '&APPID=' + apiKey;

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

		},

		getForecast: function(lat,lon){
			var deferred = $q.defer();
			var url = urlBase + 'forecast/daily?lat=' + lat + '&lon=' + lon + '&cnt=7&APPID=' + apiKey;

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



