#!/usr/bin/python3
# making the file for the post request
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    url_values = parse.urlencode({"email": email})
    full_url = url + "?" + url_values
    with request.urlopen(full_url) as resp:
        html = resp.read().decode("utf-8")
        print(html)
