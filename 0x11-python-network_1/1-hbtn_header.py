#!/usr/bin/python3
# making the file urllib first time to use
from urllib import request
from sys import argv

url = argv[1]
with request.urlopen(url) as resp:
    print(resp.getheader("X-Request-Id"))
