#!/usr/bin/python3
# making the file urllib first time to use
from urllib import request

with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    data = resp.read()
    html = data.decode("UTF-8")
    print("Body response:")
    print(f"    - type: {type(data)}")
    print(f"    - content: {data}")
    print(f"    - utf8 content: {html}")
