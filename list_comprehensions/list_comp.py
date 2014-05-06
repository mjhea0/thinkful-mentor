import time


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time

# ---- run code ---- #

test_list = xrange(1, 90000000)

comp_timer = ExecutionTime()
[num for num in test_list if num % 2 == 0]
print 'List Comprehension finished in {} seconds.'.format(comp_timer.duration())

regular_list = list()
regular_timer = ExecutionTime()
for num in test_list:
    if num % 2 == 0:
        regular_list.append(num)
print 'Regular List finished in {} seconds.'.format(regular_timer.duration())