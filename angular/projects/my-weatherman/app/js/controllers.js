angular.module('weatherApp')

.controller('rootCtrl', ['$rootScope', function($rootScope){
}])

.controller('mainCtrl', ['$rootScope','$scope','$timeout', 'weatherData', 'locationData', 
	function($rootScope, $scope, $timeout, weatherData, locationData){

		/*

		$scope.getIcon = function(){
			var icon = $day.icon;
			if (icon === 'clear-day'){
				  'clear-day': 
			}
		}

		*/


		$scope.dayOfWeek = function(i){
			var day = new Date();
			return day.setDate(day.getDate()+i);
		};

		$scope.toggle=false;

		$scope.date = new Date();
		$scope.weekdays = [];
		$scope.weekdays[0]=  "Sunday";
		$scope.weekdays[1] = "Monday";
		$scope.weekdays[2] = "Tuesday";
		$scope.weekdays[3] = "Wednesday";
		$scope.weekdays[4] = "Thursday";
		$scope.weekdays[5] = "Friday";
		$scope.weekdays[6] = "Saturday";

		var day = $scope.date.getDay();
		$scope.day = $scope.weekdays[day];

		$scope.result1 = '';
		$scope.options1 = null;
		$scope.details1 = '';

		$scope.days = [];


      	$scope.submit = function(){

      		var details = $scope.details1;
      		var coords = details.geometry;
	      		$scope.lat = coords.location.A;
	      		$scope.lon = coords.location.F;
      		
      		//retrieving the current weather 
      		weatherData.getWeather($scope.lat,$scope.lon).then(function(result) {
      			$scope.weather = result;

      			//to use in ng-repeat for forecast
      			$scope.days = result.daily.data;
      			$scope.fullAddress = details.formatted_address;

      			var current = $scope.weather.currently;

      			$scope.currentTemp = current.temperature.toFixed(1)+ '\xB0 F';
      			$scope.currentConditions = current.summary.toLowerCase();

      			var tomorrow = $scope.weather.daily.data[1];
			
				$scope.tomorrowHigh = tomorrow.temperatureMax.toFixed(1)+ '\xB0 F';
				$scope.tomorrowLow = tomorrow.temperatureMin.toFixed(1)+ '\xB0 F';


				$scope.checkTemp();
			
    
      		}).then($scope.results=true);
			
      	};


      	/*
		var useLocation = function(){
			locationData.yourLocation.then(function(data){
				var location = data.results[0];
				var name = location.address_components[7];
				$scope.zip = parseInt(name.short_name);
			});
		};
		*/

		$scope.reset = function(){
			$scope.resetColor();
			$scope.results = false;
			$scope.currentConditions = '';
			$scope.currentTemp = '';
			$scope.tomorrowHigh = '';
			$scope.tomorrowLow = '';
			$scope.result1 = '';
			$scope.options1 = null;
			$scope.details1 = '';
		};

		var toFahrenheit = function(temp){
			return parseInt(temp*(9/5)-459.67);
		};

		$scope.resetColor = function(){
		//for setting background color of page
			$rootScope.init = true;
			$rootScope.freezing = false;
			$rootScope.cold = false;
			$rootScope.mild = false;
			$rootScope.warm = false;
			$rootScope.hot = false;
		};

		//checking temperature to send to root scope, which will change bg color of site
		$scope.checkTemp = function(){
			var temp = parseInt($scope.currentTemp);

			if (temp <= 32){
				$rootScope.freezing=true;
				$rootScope.cold = false;
				$rootScope.mild = false;
				$rootScope.warm = false;
				$rootScope.hot = false;
			}
			if (temp > 32 && temp <=49){
				$rootScope.cold = true;
				$rootScope.freezing = false;
				$rootScope.mild = false;
				$rootScope.warm = false;
				$rootScope.hot = false;
			}
			if (temp>49 && temp<=65){
				$rootScope.mild = true;
				$rootScope.freezing = false;
				$rootScope.cold = false;
				$rootScope.warm = false;
				$rootScope.hot = false;
			}
			if (temp>65 && temp<=80){
				$rootScope.warm = true;
				$rootScope.freezing = false;
				$rootScope.cold = false;
				$rootScope.mild = false;
				$rootScope.hot = false;
			}
			if (temp>80) {
				$rootScope.hot = true;
				$rootScope.freezing = false;
				$rootScope.cold = false;
				$rootScope.mild = false;
				$rootScope.warm = false;
			}

		return;
	};

}])

.controller('forecastCtrl',['$scope','weatherData', function($scope, weatherData){

	$scope.forecast = null;


	
}]);
        


