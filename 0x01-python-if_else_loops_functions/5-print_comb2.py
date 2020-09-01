#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers == 99:
        print(numbers)
    else:
        print("{:02d}".format(numbers), end=", ")
