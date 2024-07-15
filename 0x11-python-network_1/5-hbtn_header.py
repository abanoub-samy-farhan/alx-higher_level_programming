#!/usr/bin/python3
"""Module Well documented"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    resp = requests.get(url)
    print(resp.headers["X-Request-Id"])
