class Calculator(object):
    def raise_on_invalid_args(self, x, y):
        number_types= (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            pass
        else:
            raise ValueError

    def add(self, x, y):
        self.raise_on_invalid_args(x,y)
        return x+y
