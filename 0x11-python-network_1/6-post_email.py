#!/usr/bin/python3
"""Module Well documented"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {
        "email": email
    }
    req = requests.post(url, params=values)
    print(req.content.decode("utf-8"))
