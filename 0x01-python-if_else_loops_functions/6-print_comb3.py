#!/usr/bin/python3
for num in range(0, 10):
    for numbers in range(0, 10):
        if (num == numbers) or (num > numbers):
            continue
        if (num == 8) and (numbers == 9):
            print("{:d}{:d}".format(num, numbers))
        else:
            print("{:d}".format(num), end="")
            print("{:d}".format(numbers), end=", ")
