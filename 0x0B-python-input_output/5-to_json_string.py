#!/usr/bin/python3
"""a function that return the JSON rep of an object str"""

import json


def to_json_string(my_obj):
    """return the JSON rep of an object
    my_obj: obj
    return: rep of an object
    """

    return json.dumps(my_obj)
