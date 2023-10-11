#!/usr/bin/python3
def common_elements(set_1, set_2):
    return list(map(lambda item: item if item in set_2 else None, set_1))
