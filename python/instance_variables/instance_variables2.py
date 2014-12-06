class Order(object):
    def __init__(self, user=None, address=None, ship_method=None):
        self.user = user
        self.address = address
        self.ship_method = ship_method
        
    def address_label(self):
        label = "method: {}\n {}\n {}".format(
                                              self.ship_method, self.user, self.address)
        return label
    
        

o = Order("Sam Halperin", "1234 Fake street", "UPS")

print o.address_label()

