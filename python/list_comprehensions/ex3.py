# reversed / iterators - ex3


alpha_list = ['A', 'B', 'C']

# reversed
rev_list = list(reversed(alpha_list))
print [i + a for i in alpha_list for a in rev_list]
print [i + a for i in alpha_list for a in reversed(alpha_list)]
rev_old = reversed(alpha_list)
print [i + a for i in alpha_list for a in alpha_list[::-1]]
rev_old = alpha_list[::-1]
print [i + a for i in alpha_list for a in rev_old]