def parent(num):

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child

foo = parent(10)
bar = parent(11)

print foo
print bar

print foo()
print bar()
