#!/usr/bin/python3
"""a function that return an obj rep by JSON"""

import json


def from_json_string(my_str):
    """a fucntion that ret an obj rep by JSON
    my_obj: obj
    return: an object
    """

    return json.loads(my_str)
