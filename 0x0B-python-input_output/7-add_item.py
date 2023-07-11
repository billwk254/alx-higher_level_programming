#!/usr/bin/python3


"""
Script: add_item

A script that adds all arguments to a Python list and saves them to a file.
"""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item():
    """
    Adds all arguments to a Python list and saves them to a file.
    """
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    data.extend(sys.argv[1:])
    save_to_json_file(data, "add_item.json")


if __name__ == "__main__":
    add_item()
