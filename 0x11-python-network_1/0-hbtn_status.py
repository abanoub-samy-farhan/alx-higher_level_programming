#!/usr/bin/python3
# making the file urllib first time to use
from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    data = resp.read()
    html = data.decode("UTF-8")
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8 content: {html}")