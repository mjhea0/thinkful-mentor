var CalendarRange = {

  DAY : 24 * 60 * 60 * 1000,

  prepareDate : function(date) {
    date = new Date(date);
    var day = date.getDay();
    return {
      date : date,
      weekday : day !== 0 && day !== 6,
      day : date.getDate(),
      month : date.getMonth(),
      year : date.getFullYear()
    };
  },

  getMonthlyRange : function(date) {
    var month = date.getMonth();
    var startDay = new Date(date);
    startDay.setDate(1);

    var firstDay = new Date(startDay);
    if (firstDay.getDay() > 0) { //Not Sunday
      firstDay.setTime(firstDay.getTime() - (firstDay.getDay() * this.DAY));
    }

    var endDay = new Date(startDay);
    if(month == 11) {
      endDay.setMonth(0);
      endDay.setYear(endDay.getFullYear() + 1);
    } else {
      endDay.setMonth(month + 1);
    }

    endDay.setTime(endDay.getTime() - this.DAY);

    var lastDay = new Date(endDay);
    lastDay.setTime(lastDay.getTime() + (6 - endDay.getDay()) * this.DAY);

    date = new Date(firstDay);
    var days = [];
    while(date <= lastDay) {
      days.push(this.prepareDate(date));
      date.setTime(date.getTime() + this.DAY);
    }

    return {
      first : firstDay,
      start : startDay,
      end : endDay,
      last : lastDay,
      days : days
    };
  },

  getDayClass : function(day, selectedMonth) {
      console.log(day);
      if( day.month == selectedMonth ){return "date-cur-month";}
      if( day.month <  selectedMonth ){return "date-prev-month";}
      if( day.month >  selectedMonth ){return "date-next-month";}
    }

};