"""
    Clock Example with class

    Given a city and an hour offset, return the local time

    - Each instance of the ClockWithClass object is initialized with:
        1. The hour offset from GMT (or UTC) time
            http://en.wikipedia.org/wiki/List_of_UTC_time_offsets
        2. The name of the city

    - Example:
        >>> from clock_with_class import *
        >>> nyc = ClockWithClass(-4, "NYC")
        >>> nyc.display()
        Local time in NYC is 19:5:6

    - Todo:
        1. Allow user to elect to have time displayed in 12 or 24hr format
        2. Refactor conversion to helper method
        3. Refactor business logic to helper method
"""

from time import time, gmtime


class ClockWithClass(object):

    # The Constructor
    def __init__(self, offsetH, city):
        # Instance attributes
        self.offsetH = offsetH
        self.city = city

    def display(self):
        """
        Returns current time, based on user-supplied offsets.
        """

        # Convert local time to GMT with gmtime() -> refactor to helper method
        self.GMTTime = gmtime(time())
        # gmtime() returns an array
        self.seconds = self.GMTTime[5]
        self.minutes = self.GMTTime[4]
        self.hours = self.GMTTime[3]

        # Calculate local time -> refactor to helper method

        # If city is ahead of GMT
        if self.offsetH >= 0:

            self.minutes = self.minutes
            self.hours = self.hours + self.offsetH

        # If city is behind GMT
        else:
            self.seconds = 60 - self.seconds
            self.minutes = self.minutes
            self.hours = self.hours + self.offsetH

        # Output
        self.local_time = "{0}:{1}:{2}".format(
            self.hours, self.minutes, self.seconds
        )
        print "Local time is {0} in {1}".format(self.local_time, self.city)
