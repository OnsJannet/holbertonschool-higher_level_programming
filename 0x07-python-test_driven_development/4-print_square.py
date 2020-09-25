#!/usr/bin/python3
def print_square(size):
    """
    print_square- Prints a Square
    @Size: where Type size must be an integer and must < 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
