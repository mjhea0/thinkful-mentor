# this module contains the classes that model a simple bike shop


# this is an "abstract" bike part,
# which contains common attributes and related methods for bike parts
class BikePart(object):

    def __init__(self, cost, weight):
        self._cost = cost
        self._weight = weight

    def get_cost(self):
        return self._cost

    def get_weight(self):
        return self._weight


# represents an "abstract" bike wheel
class Wheel(BikePart):

    def __init__(self, name, cost, weight):
        super(Wheel, self).__init__(cost, weight)
        self._name = name

    def get_name(self):
        return self._name


# represents a road wheel
class RoadWheel(Wheel):
    pass


# represents a mountain wheel
class MountainWheel(Wheel):
    pass


# represents a commuter wheel
class CommuterWheel(Wheel):
    pass


# represents an "abstract" bike frame
class Frame(BikePart):

    def __init__(self, cost, weight):
        super(Frame, self).__init__(cost, weight)


# represents an aluminum frame
class AluminumFrame(Frame):
    pass


# represents a Carbon frame
class CarbonFrame(Frame):
    pass


# represents a steel frame
class SteelFrame(Frame):
    pass


# an auxiliary class that builds a bike given the part type
class BikeBuilder(object):

    def __init__(self, manufacturer_name, num):
        self._manufacturer_name = manufacturer_name
        self._num = num

    def set_wheels(self, wheel_type):
        self._wheel_type = wheel_type

    def set_frame(self, frame_type):
        self._frame_type = frame_type

    def generate_bike(self):
        front = self._wheel_type(
            "{0} front wheel".format(self._manufacturer_name),
            self._num*27,
            self._num*1.2
        )
        back = self._wheel_type(
            "{0} back wheel".format(self._manufacturer_name),
            self._num*25,
            self._num*1.5
        )
        frame = self._frame_type(self._num*85, self._num * 3.4)
        name = "{0} Model {1}".format(self._manufacturer_name, self._num)

        return BicycleModel(name, front, back, frame)


# represents the whole bike, with parts
class BicycleModel(BikePart):

    def __init__(self, name, frontWheel, backWheel, frame):

        if(type(frontWheel) != type(backWheel)):
            raise AssertionError("Wheel types don't match")
        else:
            self._frontWheel = frontWheel
            self._backWheel = backWheel
            self._frame = frame
            self._name = name
            self._cost = self._frontWheel.get_cost() +\
                self._backWheel.get_cost() + self._frame.get_cost()
            self._weight = self._frontWheel.get_weight() +\
                self._backWheel.get_weight() + self._frame.get_weight()

    def change_cost_by_percentage(self, percentage):
        self._cost = float(self._cost) * (1+percentage)

    def __str__(self):
        return "{0} ${1} {2} lb".format(
            self._name, self.get_cost(), self.get_weight()
        )


# represents a bike manufacturer
class BicycleManufacturer(object):

    def __init__(self, name, percentage):
        self._name = name
        self._percentage = percentage

    def get_name(self):
        return self._name

    def get_percentage(self):
        return self._percentage

    def generate_bikes(self):
        bikeList = []
        frameList = [AluminumFrame, CarbonFrame, SteelFrame]
        wheelList = [RoadWheel, CommuterWheel, MountainWheel]

        for i in range(3):
            bb = BikeBuilder(self._name, i+1)
            bb.set_frame(frameList[i])
            bb.set_wheels(wheelList[i])
            bikeList.append(bb.generate_bike())

        return bikeList


# represents a bike shop
class BicycleShop(object):

    def __init__(self, name, percentage, manufacturerList):
        self._name = name
        self._percentage = percentage
        self._manufacturerList = manufacturerList
        self._inventory = []
        self.get_bikes_from_manufacturer()
        self._profit = 0

    def get_bikes_from_manufacturer(self):
        for manufacturer in self._manufacturerList:
            tempBikeList = manufacturer.generate_bikes()
            for bike in tempBikeList:
                bike.change_cost_by_percentage(manufacturer.get_percentage())
                bike.change_cost_by_percentage(self._percentage)
            self._inventory.extend(tempBikeList)

    def get_inventory(self):
        return self._inventory

    def get_name(self):
        return self._name

    def get_profit(self):
        return self._profit

    def sell_bike(self, customer, bike):
        self._inventory.remove(bike)
        customer.buy_bike(bike)
        self._profit += bike.get_cost() - (bike.get_cost()/(1+self._percentage))


# represents a customer, has the capability to buy bikes
class Customer(object):

    def __init__(self, name, funds):
        self._name = name
        self._funds = funds
        self._bike = None

    def buy_bike(self, bike):
        self._bike = bike
        self._funds -= bike.get_cost()

    def get_name(self):
        return self._name

    def get_funds(self):
        return self._funds

    def get_bike(self):
        return self._bike

    def __str__(self):
        return "{0} ${1}".format(self._name, self._funds)
