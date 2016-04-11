app.filter('flatten', function() {
  return function(arr) {
    return arr.reduce(function(a, b) {
      b.categories.forEach(function(el) {
        if(a.indexOf(el) === -1) {
          a.push(el);
        }
      });
      return a;
    }, []);
  };
});