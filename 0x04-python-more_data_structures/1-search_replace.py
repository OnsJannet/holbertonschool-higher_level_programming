#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if my_list[number] == search else my_list[number]
    for number in range(len(my_list))]
