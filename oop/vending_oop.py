class VendingMachine(object):

    # class variables
    stock = {'coca-cola': 0, 'sprite': 1,'fanta': 0}

    # instance variables
    def __init__ (self, serial_num):
        self.serial_num = serial_num

    # method
    def sell(self, item):
        if self.stock[item] > 0:
            self.stock[item] -= 1
            return self.stock
        else:
            raise Exception('empty')

    # method
    def replenish(self, item, number):
        self.stock[item] = number
        return self.stock

vending = VendingMachine(156700)
print vending.sell('sprite')
print vending.replenish('sprite', 20)
vending.sell('sprite')
vending.sell('sprite')
vending.sell('sprite')
vending.sell('sprite')
print vending.sell('sprite')
