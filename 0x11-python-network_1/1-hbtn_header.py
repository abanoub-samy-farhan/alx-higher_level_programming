#!/usr/bin/python3
"""
Module documented
"""
import urllib
from sys import argv

url = argv[1]
with urllib.request.urlopen(url) as response:
    html = response.getheader("X-Request-Id")
    print(f"{html}")
