class Car(object):

    # class attributes (what does every car have - i.e, species = 'mammal')

	# instance attributes (what is different about every car)
    def __init__(self, miles):
        self.miles = miles

	# methods (make the car, see if car is at destination)
    def drive(self, num):
        self.miles = self.miles + num
        # running total?
        return "Today we travled {} miles".format(num)

    def see_if_at_destination(self):
        # destination is 100 miles
        # pass in running total in order to see if at destination
        pass


# instantiate object
test = Car(0)
print test.drive(10)
print test.drive(12)
