#!/usr/bin/python3
"""
Class MyInt inverts operators
"""


class MyInt(int):
    """Inherit Class"""

    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
