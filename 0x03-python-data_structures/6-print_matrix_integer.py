#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for j in matrix:
            if len(j) == 0:
                print()
            for i in j:
                print("{:d}".format(i), end="\n" if i is len(j) - 1 else " ")
