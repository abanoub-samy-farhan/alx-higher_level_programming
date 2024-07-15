#!/usr/bin/python3
"""Module Well documented"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    passwrd = argv[2]
    req = requests.get(url, auth=(user, passwrd))
    try:
        print(req.json().get("id"))
    except ValueError:
        print("None a JSON file")
