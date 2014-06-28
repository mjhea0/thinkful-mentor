### Steps

*For Python 2.7x*

1. Build the base "abstract" bike part classes, identify the common attributes and methods and place them there
1. Create the concrete classes (not really anything to do inside them now though)
1. I had trouble making the bike generation automated so I made a `BikeBuilder()` class
1. Overwrite `__str__` so the classes can easily be printed
1. Make the business methods (`get_profit()` `sell_bike()`, etc.)
1. Make the main module