def parent():
    print "Printing from the parent() function."

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print first_child()
    print second_child()

parent()

first_child()
