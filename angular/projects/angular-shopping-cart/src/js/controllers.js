app.controller('mainController', ['$scope', 'dataService',
  function ($scope, dataService) {

  $scope.teaList = dataService.getTeas();
  $scope.checkoutQuantity = dataService.getCheckoutQuantity();

  $scope.addToCheckout = function(tea) {
    tea.quantity = parseInt(tea.quantity);
    tea.subtotal = parseFloat(tea.price / 100 * tea.quantity).toFixed(2);
    dataService.addToBag(tea);
    $scope.checkoutQuantity = dataService.getCheckoutQuantity();
  };

  $scope.allCategories = ['dark', 'cold', 'awesome', 'dry', 'hot', 'summer', 'lucid', 'warm', 'winter', 'spring'];

}]);

app.controller('cartController', ['$scope' , 'dataService',
  function($scope, dataService) {

  $scope.cartItems = dataService.getCheckoutBag();
  $scope.total = dataService.getTotal();
  $scope.cartQuantityOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  $scope.updateQuantity = function() {
    dataService.updateSubtotal(
      this.checkoutItem._id,
      this.selectedOption
    );
    $scope.cartItems = dataService.getCheckoutBag();
    $scope.total = dataService.getTotal();
  };

  $scope.removeItem = function() {
    dataService.updateSubtotal(this.checkoutItem._id, 0);
    $scope.cartItems = dataService.getCheckoutBag();
    $scope.total = dataService.getTotal();
  };

}]);