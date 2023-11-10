#!/usr/bin/python3
"""getting harder and harder"""


class MyList(list):
    """ a class containing the subject of the list with additions """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
