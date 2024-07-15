#!/usr/bin/python3
"""
Module documented
"""
from urllib import request
from sys import argv

if __name__ == '__main__':    
    url = argv[1]
    with request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print(f"{html}")
