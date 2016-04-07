app.service('mealDataService', function() {

  // container for meals
  var meals = [];

  // cumulative data
  var cumulativeData = {
    mealCount:0,
    tipTotal:0,
    tipAvg:0
  };

  // methods
  return {
    addMeal: function(meal) {
      meals.push(meal);
      cumulativeData.mealCount ++;
      cumulativeData.tipTotal += meal.tip;
      cumulativeData.tipAvg = (cumulativeData.tipTotal / cumulativeData.mealCount);
    },
    getMeals: function(){
      return meals;
    },
    getCumulativeData: function() {
      return cumulativeData;
    },
    resetAll: function() {
      meals.length = 0;
      cumulativeData = {
        mealCount:0,
        tipTotal:0,
        tipAvg:0
      };
    }
  };

});