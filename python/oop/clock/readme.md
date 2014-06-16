## Clock Example with class

Given a city and a hour offset, return the local time. Each instance of the ClockWithClass object is initialized with:

1. The hour offset from GMT (or UTC) time: http://en.wikipedia.org/wiki/List_of_UTC_time_offsets
1. The name of the city

### Example:

```
>>> from clock_with_class import *
>>> nyc = ClockWithClass(-4, "NYC")
>>> nyc.display()
Local time in NYC is 19:5:6
```

## Todo:

1. Allow user to elect to have time displayed in 12 or 24hr format
1. Refactor conversion to helper method
1. Refactor business logic to helper method