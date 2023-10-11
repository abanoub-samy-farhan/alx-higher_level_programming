#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy_set = a_dictionary
    list(a_dictionary)
    sorted(a_dictionary)
    for i in a_dictionary:
        print(f"{i}: {copy_set[i]}")
