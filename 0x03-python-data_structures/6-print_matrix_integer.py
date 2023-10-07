#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("$")
    else:
        for newList in matrix:
            for i in newList:
                print("{:d}".format(i), end='')
                if i != len(newList) - 1:
                    print(" ", end='')
            print("$")
