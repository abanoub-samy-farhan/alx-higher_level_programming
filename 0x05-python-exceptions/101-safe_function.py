#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error:
        error_msg = "Exception: " + str(error) + "\n"
        sys.stderr.write(error_msg)
        return None
