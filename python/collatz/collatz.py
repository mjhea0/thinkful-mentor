import time

def user_input():
    """
    loop until user enters the correct number
    """
    while True:
        try:
            number = int(raw_input("Please enter an integer: "))
            return number
        except ValueError:
            print "\nOops! That was not a valid number. Try again.\n"
            try:
                number = int(raw_input("Please enter an integer: "))
                return number
            except ValueError:
                print "\n"

def calculate(number):

    iteration = 0
    start_time = time.time()
     
    while number > 1:
        if (number % 2) == 0:
            screen_output(iteration,number,time.time())
            text_output(iteration,number,time.time())
            number = number / 2
            iteration += 1
            if number == 1:
                screen_output(iteration,number,time.time())
                break
        else:
            screen_output(iteration,number,time.time())
            text_output(iteration,number,time.time())
            number = 3 * number + 1
            iteration += 1
            if number == 1:
                screen_output(iteration,number,time.time())
                break
     
    iteration += 1
    final_iteration = iteration-1
    text_output(iteration,number,time.time())

    end_time = time.time()
    time_elapsed = end_time - start_time

    print "\nEnd at {}th iteration\nRuntime: {}".format(final_iteration, time_elapsed) 

def screen_output(iteration, number, time):
    print "{}: {} {}".format(iteration, number, time)

def text_output(iteration, number, time):
    text_file.write("{}: {} {}\n".format(iteration, number, time))


number = user_input()
text_file = open("collatz_output.txt", "w")
calculate(number)
text_file.close()
