#!/usr/bin/python3
def common_elements(set_1, set_2):
    return list(map(lambda item: item if item in set_1 and item in set_2, set_1))
