#!/usr/bin/python3
"""a function that saves object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """a fucntion that writes an obj to a txt
    using JSON rep
    my_obj: obj
    filename: filename
    return: an object
    """

    with open(filename, mode="w", encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
