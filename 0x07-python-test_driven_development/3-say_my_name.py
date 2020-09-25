#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    say_my_name - Prints The Name And The Last Name
    @first_name: where Type first_name must be a string
    @last_name: where Type last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
