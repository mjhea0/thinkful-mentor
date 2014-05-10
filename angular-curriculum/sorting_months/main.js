console.log("whee!")

angular.module('myApp', []).
controller('myCtrl', function($scope) {
   var months = [ 
    {english: 'August',
    french: 'Aout',
    days: 31,
    ordinal: 8,
     season: 'summer'
   },
   {english: 'March',
    french: 'Mars',
    days: 31,
    ordinal: 3,
    season: 'spring'
   },
  {english: 'February',
    french: 'Fevrier',
    days: 28,
    ordinal: 2,
   season: 'winter'
   },
  {english: 'April',
    french: 'Avril',
    days: 30,
    ordinal: 4,
   season: 'spring'
   },
  {english: 'May',
    french: 'Mai',
    days: 31,
    ordinal: 5,
   season: 'spring'
   },
  {english: 'January',
    french: 'Janvier',
    days: 31,
    ordinal: 1,
   season: 'winter'
   },
  {english: 'September',
    french: 'Septembre',
    days: 30,
    ordinal: 9,
   season: 'fall'
   },
  {english: 'October',
    french: 'Octobre',
    days: 31,
    ordinal: 10,
   season: 'fall'
   },
  {english: 'November',
    french: 'Novembre',
    days: 30,
    ordinal: 11,
   season: 'fall'
   },
  {english: 'December',
    french: 'Decembre',
    days: 31,
    ordinal: 12,
   season: 'winter'
   },
  {english: 'June',
    french: 'Juin',
    days: 30,
    ordinal: 6,
   season: 'summer'
   },
  {english: 'July',
    french: 'Juillet',
    days: 31,
    ordinal: 7,
   season: 'summer'
   }
  ];  
  $scope.months = months;
});