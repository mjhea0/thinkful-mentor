def genarators_using_yield(till):
    current_num = 0
    while current_num < till:
        yield current_num
        current_num += 1


for value in genarators_using_yield(10):
	print(value)
