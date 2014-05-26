# intro - ex2


def create_list(alpha_list):
    # Read statements, left to right
    return [letter for letter in alpha_list if filter(letter)]


def filter(letter):
    return letter >= 'B'


alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print create_list(alpha_list)