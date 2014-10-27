
class Calculator(object):

    def calc_discount(self, total, discount, discount_type):
        if discount_type == "percentage":
            if discount < 100:
                return total * (discount * .01)
            else:
                raise ValueError("Discount cannot be greater than 100")
        elif discount_type == "dollar":
            if discount <= total:
                return total - (total - discount)
            else:
                raise ValueError("Discount cannot be greater than the total")
        else:
            raise ValueError("Please enter a correct discount type.")

calc = Calculator()
result = calc.calc_discount(100, 10, "dollar")
print result
