import sys
import pdb

random1=['1','2','3','4','5','6','7','8','9','10','11','12'] 
random2=['1','2','3','4','5','6','7','8','9','10','11','12'] 

from random import choice 

while True: 
    print "To exit this game type 'exit'" 
    pdb.set_trace()
    answer = raw_input("What is " + choice(random2) + " times " + choice(random1) + "? ") 
    # exit
    if answer == "exit":
        print "Now exiting game!"
        sys.exit() 

    # determine if number is correct
    elif answer == int(choice(random2))*int(choice(random1)):
        print "Correct!"
    else:
       print "Wrong!"
