#!/usr/bin/env python3
# that takes one argument, length, representing the desired length of the Fibonacci sequence.
def print_fibonacci(length):
    # initializes an empty list called my_list, which will store the Fibonacci sequence.
    my_list = []
    #checks if the desired length is greater than zero. If so, it appends the first Fibonacci number, 0, to my_list.
    if length > 0:
        my_list.append(0)
        #checks if the desired length is greater than or equal to 2. If so, it appends the second Fibonacci number, 1, to my_list.
    if length >= 2:
        my_list.append(1)
        #This loop iterates starting from the third element (index 2) up to the desired length (length). It appends the sum of the last two elements of my_list to my_list, effectively generating the next Fibonacci number in the sequence.
        for i in range(2, length):
            my_list.append(my_list[-1] + my_list[-2])
    print(my_list)
    