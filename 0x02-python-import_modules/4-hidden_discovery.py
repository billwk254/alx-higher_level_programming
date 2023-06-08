#!/usr/bin/python3
import hidden_4

def print_names():
    for name in sorted(dir(hidden_4)):
        if name[:2] != '__':
            print("{}".format(name))

if __name__ == "__main__":
    print_names()
