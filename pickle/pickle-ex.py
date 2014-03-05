import pickle

# write
my_list = ['t', 'i', 'm', 'o', 't', 'h', 'y', 1, 1, 2, 2, 8, 2]
with open('save.txt','wb') as file:
    pickle.dump(my_list,file)

# read
with open('save.txt','rb') as file:
    my_dict = pickle.load(file)
print my_dict
