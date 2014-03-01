# determine if the driver is at the destination

class RoadTrip(object):

    def __init__(self, starting_miles):
        self.starting_miles = starting_miles  

    def get_miles(self):
        """ ask for miles drove that day."""
        
        num = float(raw_input("\nHow many miles did you travel today? "))
        return num

    def calculate_total(self, miles_driven, cumulative_total):
        """ determine total cumulative miles driven """

        cumulative_total = self.starting_miles + miles_driven + cumulative_total
        return cumulative_total
        
    def output_total_driven(self, miles_driven, cumulative_total):
        """ output miles driven """

        return "\nToday, you traveled {} miles! You have traveled a \
total of {} miles!\n".format(miles_driven, cumulative_total)

    def calculate_miles_remaining(self, cumulative_total):
        """ calculate the number of miles to destination """

        remaining = cumulative_total - 100
        if remaining > 0:
            return "However, you are {} miles past our destination. Go back.".format(remaining)
        elif remaining < 0:
            return "Sorry. Not there yet. {} miles to go.".format(remaining*-1)
        else:
            return "You made it!"


# --------------------------------- #

def main():
    create = RoadTrip(0) # starting miles
    total = 0
    while total < 100:
        total_driven_today = create.get_miles()
        total = create.calculate_total(total_driven_today, total)
        print create.output_total_driven(total_driven_today, total)
        print create.calculate_miles_remaining(total) 

if __name__ == '__main__':
    main()


