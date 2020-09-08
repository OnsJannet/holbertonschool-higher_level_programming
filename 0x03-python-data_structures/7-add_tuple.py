#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = tuple_a or (0, 0)
    len_b = tuple_b or (0, 0)
    if len(tuple_a) < 2:
        len_a += (0, 0,)
    if len(tuple_b) < 2:
        len_b += (0, 0,)
    new_tuple = (len_a[0] + len_b[0], len_a[1] + len_b[1])
    return new_tuple
