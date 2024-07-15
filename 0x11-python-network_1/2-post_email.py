#!/usr/bin/python3
# making the file for the post request
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    url_values = parse.urlencode({"email": email})
    url_values = url_values.encode("ascii")
    req = request.Request(url, url_values)
    with request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
        print(html)
