describe("FilterModule", function() {
  beforeEach(module("FilterModule"));

  describe("even filter", function() {
    it('should only return even numbers', inject(function(evenFilter) {
      expect(evenFilter([1,2,3,4])).toEqual([2,4]);
    }));
  });
});