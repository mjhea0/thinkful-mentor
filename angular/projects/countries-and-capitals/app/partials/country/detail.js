angular.module('cncApp').controller('detailCtrl', 
    ['$scope', 'cncData', '$state', '$stateParams', '$q',
    function($scope, cncData, $state, $stateParams, $q){
        var detailCountry = $stateParams.countryCode.toUpperCase();
        //Get the countries data if not already available:
        //This enables entering the app directly into a detail view.
        $q.when(cncData.countries).then(function(result){
            //If cncData.countries is still a promise...
            if(toString.call(cncData.countries)=='[object Object]') {
                //...replace it with the returned array.
                cncData.countries = result.geonames;
                cncData.index = result.index;
            }
            $scope.country = cncData.countries[cncData.index[detailCountry]];
        });
        $scope.flag = detailCountry.toLowerCase();
        $scope.map = detailCountry;
        cncData.getCapitalInfo(detailCountry).then(function(result){
            $scope.capital = result;
        });
        cncData.getNeighbors(detailCountry).then(function(result){
            $scope.numNeighbors = result.totalResultsCount;
            $scope.neighborList = result.geonames;
        });
  }]);