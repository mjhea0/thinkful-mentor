# chained and nested loops - ex3

num_list = [2, 4, 6]
alpha_list = ['A', 'B', 'C']

print "\n# 1) ------------ #\n"

# chain
print ['{}-{}'.format(letter, number) for letter in alpha_list for number in num_list]

# nest
beta_list = []
for letter in alpha_list:
    for number in num_list:
        beta_list.append('{}-{}'.format(letter, number))

print beta_list

print "\n# 2) ------------ #\n"

# chain
print [['{}-{}'.format(letter, number) for letter in alpha_list] for number in num_list]

# nest
beta_list = []
for number in num_list:
    beta_list_inner = []
    for letter in alpha_list:
        beta_list_inner.append('{}-{}'.format(letter, number))
    beta_list.append(beta_list_inner)
print beta_list

print "\n# 3) ------------ #\n"

# chain
print ['{}-{}'.format(letter, number) for letter in alpha_list if letter < 'C' for number in num_list if number < 5]
print ['{}-{}'.format(letter, number) for letter in alpha_list for number in num_list if number < 5 and letter < 'C']


# nest
beta_list = []
for letter in alpha_list:
    if letter < 'C':
        for number in num_list:
            if number < 5:
                beta_list.append('{}-{}'.format(letter, number))
print beta_list

beta_list = []
for letter in alpha_list:
    for number in num_list:
        if number < 5 and letter < 'C':
            beta_list.append('{}-{}'.format(letter, number))
print beta_list