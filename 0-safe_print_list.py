#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lenght = x if x < len(my_list) else len(my_list)
    for i in range(lenght):
        print("{:d}".format(my_list[i]), end="")
    print("")
    return lenght
