#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        list_of_values = list(a_dictionary.values())
        return max(list_of_values)
