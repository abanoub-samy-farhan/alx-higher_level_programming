#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        value = 0
        try:
            value = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            pass
        except ZeroDivisionError:
            print("division by 0")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            new_list.append(value)
        i += 1
    return new_list
