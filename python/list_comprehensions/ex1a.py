# intro - ex1a


def create_list(alpha_list):
    beta_list = []
    for letter in alpha_list:
        if filter(letter):
            beta_list.append(letter)
    return beta_list


def filter(letter):
    return letter >= 'B'


alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print create_list(alpha_list)