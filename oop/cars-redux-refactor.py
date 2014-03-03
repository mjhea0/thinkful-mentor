class Car(object):

    def __init__(self, color, speed, cop):
        self.color = color
        self.speed = speed
        self.cop = cop

    def accelerate(self, amount=10, car_speed=0):
        accelerate = []
        new_speed = self.speed + amount + car_speed
        accelerate.extend([new_speed,"\nYour {} car accelerated to {}.".format(self.color, new_speed)])
        return accelerate

    def check_speed(self, current_speed):
        if current_speed > 70:
            return "You're speeding! Watch out for cops!"
        else:
            return "You're under the speed limit."

    def pulled_over(self):
        if self.cop == True:
            return "Cop! You got pulled over. Bummer."
        else:
            return "No cops. Speed all you want!"


# ----------- #

my_car = Car("red",10, True)
speed = my_car.accelerate(50)
print speed[1]
print my_car.check_speed(speed[0])
speed = my_car.accelerate(20, speed[0])
print speed[1]
print my_car.check_speed(speed[0])
speed = my_car.accelerate(-60, speed[0])
print speed[1]
print my_car.check_speed(speed[0])

print "\n------------"

my_blue_car = Car("blue",40, True)
speed = my_blue_car.accelerate(10)
print speed[1]
print my_blue_car.check_speed(speed[0])
speed = my_blue_car.accelerate(20, speed[0])
print speed[1]
print my_blue_car.check_speed(speed[0])
speed = my_blue_car.accelerate(40, speed[0])
print speed[1]
print my_blue_car.check_speed(speed[0])


# ----------- #

"""
To Do -


Use logic to deterime that if a cop is nearby, you will get pulled over if you are speeding. 
Otherwise you're in the clear.
2. Change the "accelerate()" method to show whether a car has accelerated or decelerated.
"""


