#!/usr/bin/python3


"""
This script takes a URL and an email address as arguments, sends a POST
to the URL with the email as a parameter, and displays the body
"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print("Email:", email)
    print(response.text)
