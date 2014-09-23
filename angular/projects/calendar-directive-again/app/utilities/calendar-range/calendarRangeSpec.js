describe('CalendarRange', function() {

  beforeEach(function() {
    this.addMatchers({
      toMatchDate: function(expected) {
        if(typeof expected == 'string') {
          var date = expected.split('-');
          expected = new Date(date[0], date[1], date[2]);
        }

        var actual = this.actual;
        return actual.getMonth()    == expected.getMonth()    &&
               actual.getFullYear() == expected.getFullYear() &&
               actual.getDate()     == expected.getDate();
      }
    });
  });

  it('should return the proper object for the given date', function() {
    var date = new Date();
    var prepared = CalendarRange.prepareDate(date);

    var day = date.getDate();
    expect(prepared.weekday).toBe(day !== 0 && day !== 6);
    expect(prepared.day).toBe(date.getDate());
    expect(prepared.year).toBe(date.getFullYear());
    expect(prepared.month).toBe(date.getMonth());
    expect(prepared.date).toEqual(date);
  });

  it('should return a valid date range for Feb 2014', function() {
    // we know for sure that this month is what it is in terms of dimensions
    var date = new Date(2014, 1, 10);

    var range = CalendarRange.getMonthlyRange(date);

    expect(range.first) .toMatchDate('2014-0-26');
    expect(range.start) .toMatchDate('2014-1-1');
    expect(range.end)   .toMatchDate('2014-1-28');
    expect(range.last)  .toMatchDate('2014-2-1');

    expect(range.days.length).toBe(35);

    for(var i=0;i<range.days.length;i++) {
      var current = range.days[i];
      expect(CalendarRange.prepareDate(current.date)).toEqual(current);
    }
  });

  it('should return the appropriate class for the day based on the month selected for the calendar', function(){
    var date = new Date(2014, 7, 17);
    var day = {
      date : date,
      weekday : false,
      day : 17,
      month : 7,
      year : 2014
    };
    var selectedMonth = 6;

    var result = CalendarRange.getDayClass(day, selectedMonth);
    var expected = "date-next-month";
    expect(result).toEqual(expected);

    day.month = 5;
    result = CalendarRange.getDayClass(day, selectedMonth);
    expected = "date-prev-month";
    expect(result).toEqual(expected);

    day.month = 6;
    result = CalendarRange.getDayClass(day, selectedMonth);
    expected = "date-cur-month";
    expect(result).toEqual(expected);

  });

});