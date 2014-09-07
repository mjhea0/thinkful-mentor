// globals
totalRows = 2;

angular.module('yay', []).
  controller('LineCtrl', function($scope) {
    $scope.rows = [
      {id: 1, item:'mentoring', description: 'angular+karma+jasmine', rate: 30, hours: 1},
      {id: 2, item:'consulting', description: 'node+mocha+chai', rate: 40, hours: 3},
    ];

    $scope.addRow = function() {
      totalRows += 1;
      $scope.rows.push( {id: totalRows} );
      console.log($scope.rows);
    };
    $scope.removeRow = function(id) {
      for (i = 0; i < $scope.rows.length; i++) {
        if ($scope.rows[i].id === id) {
          $scope.rows.splice(i, 1);
        }
      }
    };
  });





