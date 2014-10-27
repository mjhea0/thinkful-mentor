def calculate_discount(item_cost, relative_discount, absolute_discount):
    """ Discount an item first by relative_discount and
        then discount new total again by absolute_discount """
    if item_cost <= 0:
        return 0
    else:
        # calculate relative discount
        relative_discount_amount = item_cost * (float(relative_discount)/100)
        # calculate total after relative discount
        after_relative_discount = item_cost - relative_discount_amount
        # calculate total after relative discount AND absolute discount
        discounted_total = after_relative_discount - absolute_discount

        if discounted_total < 0:
            return 0
        else:
            return discounted_total


def main():
    discounted_total = calculate_discount(200, 10, 30)
    print discounted_total

if __name__ == "__main__":
    main()
