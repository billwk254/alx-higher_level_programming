#!/usr/bin/python3


"""
This script takes a URL as an argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header
of the response.
"""


import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            header = response.headers.get("X-Request-Id")
            print(header)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
