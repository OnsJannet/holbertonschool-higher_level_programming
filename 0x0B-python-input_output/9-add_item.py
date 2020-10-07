#!/usr/bin/python3
"""a function that adds all arguments to Pythonlist
and save them to a file"""

from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


try:
    new_list = load_from_json_file('./add_item.json')
except Exception:    # except Exception
                            # to silince pep8 : E722 do not use bare except'
    new_list = []
for i in range(1, len(argv)):
    new_list.append(argv[i])
save_to_json_file(new_list, './add_item.json')
