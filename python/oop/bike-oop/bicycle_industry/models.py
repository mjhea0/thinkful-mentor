class Wheel(object):
    def __init__(self, weight, cost, name):
        self.weight = weight
        self.cost = cost
        self.name = name

class Frame(object):
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

class Bicycle(object):
    def __init__(self, f_wheel, r_wheel, frame, name, mfg):
        self.f_wheel = f_wheel
        self.r_wheel = r_wheel
        self.frame = frame
        self.name = name
        self.mfg = mfg

    def weight(self):
        return self.f_wheel.weight + self.r_wheel.weight + self.frame.weight

    def wholesale_cost(self):
        material_cost = self.f_wheel.cost + self.r_wheel.cost + self.frame.cost
        return  material_cost + material_cost * (self.mfg.margin/100)

class Manufacturer(object):
    def __init__(self, margin, name):
        self.margin = margin
        self.name = name
        self.inventory = []

    def add_inventory(self, frame, wheel, name):
        b = Bicycle(wheel, wheel, frame, name, self)
        self.inventory.append(b)

    def ship(self, n):
        shipment = []
        while n > 0 and len(self.inventory) >0:
            shipment.append(self.inventory.pop())
            n -= 1
        return shipment
        

class BikeShop(object):
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = []
        self.sold = []

    def restock(self, new_bikes):
        for b in new_bikes:
            self.inventory.append(b)

    def retail_price(self, bike):
        return bike.wholesale_cost() + bike.wholesale_cost() * (float(self.margin)/100)

    def print_stock(self):
        for i, b in enumerate(self.inventory):
            print "{} {}: {}".format(i, b.name, self.retail_price(b))

    def print_filtered_stock(self, customer):
        print "{} with a budget of {} can afford: ".format(customer.name, customer.budget)
        for i, b in enumerate(self.inventory):
            if self.retail_price(b) <= customer.budget:
                print "{} {}: {}".format(i, b.name, self.retail_price(b))

    def sell(self, i):
        bike_sold = self.inventory.pop(i)
        self.sold.append(bike_sold)
        return bike_sold

    def total_sales(self):
        total_wholesale = 0
        total_retail = 0
        for b in self.sold:
            total_wholesale += b.wholesale_cost()
            total_retail = self.retail_price(b)

        return total_retail - total_wholesale

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget