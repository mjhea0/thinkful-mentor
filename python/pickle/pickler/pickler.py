import pickle

def do_pickle(data, filename):
    pickle.dump(data, open(filename, "wb"))

def unpickle(filename):
    return pickle.load(open(filename, "rb") )