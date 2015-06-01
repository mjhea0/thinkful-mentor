angular.module('directives',[])


.directive('sevenDay', function(){
    return {
        restrict:'EA',
        scope: true,
        templateUrl:'partials/sevenDay.html',
        link: function(scope,element,attrs){

        }
    };
})



.directive('sliding-bar', function(){
	return {
		templateUrl: 'slidingbar.html',
		restrict: 'E'
	};
})



.directive('tooltip', function(){
    return {
        restrict: 'A',
        link: function(scope, element, attrs){
            $(element).hover(function(){
                // on mouseenter
                $(element).tooltip('show');
            }, function(){
                // on mouseleave
                $(element).tooltip('hide');
            });
        }
    };
});