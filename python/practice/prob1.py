"""

The squirrels in Palo Alto spend most of the day playing. 
In particular, they play if the temperature is between 60 and 90 (inclusive). 
Unless it is summer, then the upper limit is 100 instead of 90. 
Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise. 

"""


def squirrels(temperature, is_summer):
    if temperature >= 60 and temperature <= 90:
        return True
    elif is_summer == True:
        if temperature >= 60 and temperature <= 100:
            return True
        else:
            return False
    else:
        return False



# ----- run code ----- #

print squirrels(80, True) == True
print squirrels(80, False) == True
print squirrels(100, True) == True
print squirrels(100, False) == False
print squirrels(50, True) == False
print squirrels(50, False) == False
print squirrels(120, True) == False
print squirrels(120, False) == False
