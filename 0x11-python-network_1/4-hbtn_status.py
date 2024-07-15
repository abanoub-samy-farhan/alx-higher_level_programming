#!/usr/bin/python3
"""Module Well documented"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    resp = requests.get(url)
    content = resp.content
    content = content.decode("utf-8")
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- utf-8: {content}")