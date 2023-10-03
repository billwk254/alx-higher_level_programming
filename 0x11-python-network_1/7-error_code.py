#!/usr/bin/python3


"""
This script takes a URL as an argument, sends a request to the URL,
and displays the body of the response. If the HTTP status code is greater
than or equal to 400, it prints an error message with the status code.
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
