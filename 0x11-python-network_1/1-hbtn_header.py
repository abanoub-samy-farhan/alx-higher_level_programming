#!/usr/bin/python3
"""
Module documented
:"""
from urllib import request
from sys import argv

url = argv[1]
with request.urlopen(url) as resp:
    print(resp.getheader("X-Request-Id"))
