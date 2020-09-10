#!/usr/bin/python3
def weight_average(my_list=[]):
    i, j = 0, 0
    if my_list:
        tupl = ()
        for tupl in my_list:
            i += (tupl[0] * tupl[1])
            j += tupl[1]
        return i / j
    return 0
