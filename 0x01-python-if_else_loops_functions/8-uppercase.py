#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print(c, end='')
    print()
