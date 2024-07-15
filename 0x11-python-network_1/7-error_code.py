#!/usr/bin/python3
"""Module Well documented"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if req.status_code != 200:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)