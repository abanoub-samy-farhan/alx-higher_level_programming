#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for lis in matrix:
        sub_list = []
        for i in lis:
            sub_list.append(i * i)
        new_list.append(sub_list)
    return new_list

