import os

with open("hello.txt", "r") as hello_file:
    for line in hello_file:
        print line ,


with open("test.txt", "w") as test_file:
    test_file.write("This is a test!\n")


with open("test.txt", "a") as test_file:
    test_file.write("One more thing!")
