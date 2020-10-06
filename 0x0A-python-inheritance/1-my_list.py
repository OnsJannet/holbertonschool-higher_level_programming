#!/usr/bin/python3
"""
a function that prints a sorted list inherited from list
"""


class MyList(list):
    def print_sorted(self):
        """
        prints a sorted list in an ascending order
        """
        print(sorted(self))
