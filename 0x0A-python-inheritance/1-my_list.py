#!/usr/bin/python3
"""
a function that prints a sorted list inherited from list
"""


class MyList(list):

    """
    prints a sorted list in an ascending order
    """
    def print_sorted(self):
        print(sorted(self))
