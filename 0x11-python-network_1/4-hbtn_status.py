#!/usr/bin/python3
"""Module Well documented"""
import requests

if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    content = resp.content
    content = content.decode("utf-8")
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- utf-8: {content}")