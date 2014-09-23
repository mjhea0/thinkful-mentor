console.log("app.js loaded.");
angular.module('calendarDemoApp', [])
    .controller('calendarCtrl', function($scope){
        console.log("controller loaded");

    })
    .directive('mySimpleCalendar', function(){
        return {
            restrict: 'E',
            templateUrl: 'my-simple-calendar.html',
            link: function($scope, element, attr){
                console.log('directive initialized!');

                $scope.setMonth = function(monthNum) {
                    console.log("setting the month to:." + monthNum);
                    $scope.selectedMonth = monthNum;
                    $scope.loadCalendar();
                };

                $scope.setYear = function(yearNum){
                    console.log("setting the year to:." + yearNum);
                    $scope.selectedYear = yearNum;
                    $scope.loadCalendar();
                };
                $scope.loadCalendar = function(){
                    console.log('loading calendar using month: ' + $scope.selectedMonth + ' year: ' + $scope.selectedYear);

                    var calendarDate = new Date($scope.selectedYear, $scope.selectedMonth, 1, 0, 0, 0, 0);

                    $scope.range = CalendarRange.getMonthlyRange(calendarDate);
                    console.log("weeksInCalendar: " + Math.ceil($scope.range.days.length/7));
                    var weeksInCalendar = Math.ceil($scope.range.days.length/7);
                    $scope.weeks =  new Array(weeksInCalendar);
                    console.log("weeks.length: " + $scope.weeks.length);
                    var firstDayInWeek = 0;
                    for(var i = 0; i < $scope.weeks.length; i++){
                        var ind = Math.floor(i);
                        $scope.weeks[Math.floor(ind)] = {};
                        var lastDayInWeek = (ind+1)*7;
                        console.log("slicing from: " + firstDayInWeek + " to " + lastDayInWeek);
                        $scope.weeks[ind].days = $scope.range.days.slice(firstDayInWeek,lastDayInWeek);
                        firstDayInWeek  = lastDayInWeek;
                        console.log("testing loop " + i);
                    }

                    for (var k = 0; k < $scope.weeks.length; i++) {
                        for(var j = 0; j < $scope.weeks[k].days.length; j++){
                            $scope.weeks[k].days[j].cssclass = CalendarRange.getDayClass($scope.weeks[k].days[j], $scope.selectedMonth);
                        }
                    }
            // console.log($scope.range);
            // console.log($scope.weeks);
        };

        var currentDate = new Date();
        // console.log( currentDate.getMonth() );
        $scope.setMonth(currentDate.getMonth());
        $scope.setYear(currentDate.getFullYear());
        $scope.loadCalendar();

    }
        };
    });