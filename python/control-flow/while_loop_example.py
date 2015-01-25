"""

Problem:


Use a while loop to solve the following problem:
A slow, but determined, walker sets off from Leicester
to cover the 102 miles to London at 2 miles per hour.
Another walker sets off from London heading to Leicester
going at 1 mile per hour.

Where do they meet?

------

Distance = rate x time
time = distance / rate

Speed of Walker 1: 2 mph
Speed of Walker 2: 1 mph
Distance: 102 miles

2t + 1t = 102
102 / 3 = 34

Walkers will meet 34 minutes after departing

2 * 34 = 68
1 * 34 = 34

So, they meet 68 miles from Leicester and 34 miles from London

"""

miles_traveled = 0

while True:
    if (2 * miles_traveled) + (miles_traveled) == 102:
        print 2*miles_traveled
        break
    else:
        miles_traveled += 1


position_a = 0
position_b = 102

while position_a < position_b:
    position_a += 2
    position_b -= 1

print position_a
