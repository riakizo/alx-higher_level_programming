#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)."""
    sum = 0
    for a in set(my_list):
        sum += a
    return sum
