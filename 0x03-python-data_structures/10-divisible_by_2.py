#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = [True if element % 2 == 0 else False for element in my_list]
    return newlist
