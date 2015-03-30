angular.module('cncApp').controller('countriesDataCtrl', 
    ['$scope', 'cncData', '$q',
    function($scope, cncData, $q){
        var toString = Object.prototype.toString;
        //Bind the countries data onto $scope when it becomes available:
        $q.when(cncData.countries).then(function(result){
            //If cncData.countries is still a promise...
            if(toString.call(cncData.countries)=='[object Object]') {
                //...replace it with the returned array.
                cncData.countries = result.geonames;
                cncData.index = result.index;
            }
            $scope.countries = cncData.countries;
        });
    //Source: Filipp Lepalaan - http://stackoverflow.com/questions/14713622/twitter-bootstrap-row-filter-search-box
    $(document).ready(function () {
        (function ($) {
            $('#filter').keyup(function () {
                var rex = new RegExp($(this).val(), 'i');
                $('.searchable tr').hide();
                $('.searchable tr').filter(function () {
                    return rex.test($(this).text());
                }).show();
            });
        }(jQuery));
    });
    //Set focus onto input.
    document.getElementById("filter").focus();
}]);