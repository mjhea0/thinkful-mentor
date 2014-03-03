class Car(object):

    def __init__(self, color, cop):
        self.color = color
        self.cop = cop

    def accelerate(self, amount=10, car_speed=0):
        accelerate = []
        new_speed =  amount + car_speed
        accelerate.append(new_speed)
        if amount >= 0:
            accelerate.append("\nYour {} car accelerated to {}.".format(self.color, new_speed))
        else:
            accelerate.append("\nYour {} car decelerated to {}.".format(self.color, new_speed))
        return accelerate

    def check_speed(self, current_speed):
        if current_speed > 70:
            return "You're speeding! Watch out for cops!"
        else:
            return "You're under the speed limit."

    def pulled_over(self, speed):
        if self.cop == True and speed > 70:
            return "Cop! You got pulled over. Bummer."
        else:
            return "No cops. Speed all you want!"


# ----------- #

my_car = Car("red", True)
speed = my_car.accelerate(50)
print speed[1]
print my_car.check_speed(speed[0])
print my_car.pulled_over(speed[0])
speed = my_car.accelerate(20, speed[0])
print speed[1]
print my_car.check_speed(speed[0])
print my_car.pulled_over(speed[0])
speed = my_car.accelerate(-60, speed[0])
print speed[1]
print my_car.check_speed(speed[0])
print my_car.pulled_over(speed[0])

print "\n------------"

my_blue_car = Car("blue", True)
speed = my_blue_car.accelerate(10)
print speed[1]
print my_blue_car.check_speed(speed[0])
print my_blue_car.pulled_over(speed[0])
speed = my_blue_car.accelerate(20, speed[0])
print speed[1]
print my_blue_car.check_speed(speed[0])
print my_blue_car.pulled_over(speed[0])
speed = my_blue_car.accelerate(40, speed[0])
print speed[1]
print my_blue_car.check_speed(speed[0])
print my_blue_car.pulled_over(speed[0])
speed = my_blue_car.accelerate(20, speed[0])
print speed[1]
print my_blue_car.check_speed(speed[0])
print my_blue_car.pulled_over(speed[0])

# ----------- #

"""
To Do -
1. Change the "accelerate()" method to show whether a car has accelerated or decelerated.
"""


