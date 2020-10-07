#!/usr/bin/python3
"""a function that creat obj from JSON file"""

import json


def load_from_json_file(filename):
    """a fucntion that creats obj from JSON
    filename: filename
    """

    with open(filename, mode="r", encoding='utf-8') as my_file:
        return json.load(my_file)
