#!/usr/bin/python3


def add_integer(a, b):
    """function add_integer returns the sum of two integers
    isinstance : checks
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        raise TypeError("{:} must be an integer"
                        .format('b' if isinstance(a, (int, float)) else 'a'))
