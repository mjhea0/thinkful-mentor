var app = angular.module('myApp', []);

app.controller('myCtrl', function ($scope) {

  $scope.employees = [
    {name:'Seth', phone:'456-1212', salary:'60123'},
    {name:'Jon', phone:'456-9876', salary:'6123'},
    {name:'Chris', phone:'456-4321', salary:'9123'},
    {name:'Adam', phone:'456-5678', salary:'20000'},
    {name:'Julie', phone:'456-8765', salary:'40000'}
  ];

  $scope.predicate = '-salary';


  angular.forEach($scope.employees, function (employee) {
    employee.salary = parseFloat(employee.salary);
  });

});



