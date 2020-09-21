#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = my_list.count('0')
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end='')
            count += 1
        except Exception:    # except Exception
                            # to silince pep8 : E722 do not use bare except'
            break
    print()
    return count
