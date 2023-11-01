#!/usr/bin/python3

class static_variable:
    count = 0

def magic_string():
    static_variable.count += 1
    string = "BestSchool, " * static_variable.count
    return string[:-2]
