#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) >= 65 and ord(upper) <= 90:
            upper = chr(ord(upper) + 32)
        print("{}".format(upper), end="")
    print()
