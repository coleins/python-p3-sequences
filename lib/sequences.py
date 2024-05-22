#!/usr/bin/env python3
length =10
def print_fibonacci(length):
    my_list = []
    if length > 0:
        my_list.append(0)
    if length >= 2:
        my_list.append(1)
        for i in range(2, length):
            my_list.append(my_list[-1] + my_list[-2])
    print(my_list)
    