#!/usr/bin/python3
"""Module Well documented"""
from urllib import request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            print(data)
    except HTTPError as e:
        print(f"Error code: {e.code}")
