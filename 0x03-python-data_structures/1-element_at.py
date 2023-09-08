#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    for i in my_list:
        if idx < 0:
            return "None"
        elif idx >= n:
            return "None"
        else:
            return my_list[idx]
