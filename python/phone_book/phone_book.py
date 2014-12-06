import pickle
import os.path
import sys

class PhoneBook(object):
    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(filename):
            self.__store_pb({})

    def __repr__(self):
        r = ""
        for name, number in self.__load_pb().iteritems():
            r += "{} => {}\n".format(name, number)
        if r: 
            return r
        else:
            return "no numbers stored"

    def __load_pb(self):
        return pickle.load(open (self.filename, 'rb'))

    def __store_pb(self, data):
        pickle.dump(data, open(self.filename, 'wb'))
    
    def update(self, name, number):
        pb = self.__load_pb()
        pb[name] = number
        self.__store_pb(pb)
        return "stored"

    def delete(self, name):
        pb = self.__load_pb()
        if pb.has_key(name):
            del pb[name]
            self.__store_pb(pb)
            return "{} delted".format(name)
        else:
            return "not found"

    def query(self, name):
        pb = self.__load_pb()
        if pb.has_key(name):
            return "{} => {}".format(name, pb[name])
        else:
            return "not found"

def usage():
    usage = """
python phone_book.py <command> [args]
commands:
    print:  print the phonebook
    delete: <name>: delete a name from the phonebook
    add:    <name> <number>: add name and number
    update: <name> <number>: change someones number
"""
    print usage
    sys.exit(0)

def main():
    FILENAME = "pb_data.p"
    pb = PhoneBook(FILENAME)

    command = None
    name = None
    number = None
    try:
        command = sys.argv[1]
        name = sys.argv[2]
        number = sys.argv[3]
    except IndexError:
        pass

    if command == 'print':
        print pb
    elif command == 'delete':
        if not name:
            usage()
        print pb.delete(name)
    elif command == 'add' or command == 'update':
        if not (name and number):
            usage()
        print pb.update(name, number)
    elif command == 'query':
        if not name:
            usage()
        print pb.query(name)
    else:
        usage()

if __name__ == "__main__":
    main()