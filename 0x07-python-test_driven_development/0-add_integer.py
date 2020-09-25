#!/usr/bin/python3


def add_integer(a, b=98):
    """
    add_integer - Adss Two Integers
    @a: where Type a must be an integer
    @b: where Type b must be an integer
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        raise TypeError("{:} must be an integer"
                        .format("b" if isinstance(a, (int, float)) else "a"))
