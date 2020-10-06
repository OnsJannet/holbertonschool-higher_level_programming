#!/usr/bin/python3
"""
Class MyInt inverts operators
"""


class MyInt(int):
    def __eq__(self, other):
        """
        to change the == sign to !=
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """
        to Changes  the != to ==
        """
        return int(self) == int(other)
