#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as te:
        error_msg = "Exception: " + str(te) + "\n"
        sys.stderr.write(error_msg)
        return False
