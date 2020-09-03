#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv) - 1
    if l == 0:
        print("{:d} arguments.".format(l))
    elif l == 1:
        print("{:d} argument:".format(l))
    else:
        print("{:d} arguments:".format(l))
    for i in range(l):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
