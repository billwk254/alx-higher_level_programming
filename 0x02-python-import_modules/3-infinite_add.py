#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from arguments

    if len(args) == 0:
        print(0)
    else:
        result = sum(int(arg) for arg in args)
        print(result)
