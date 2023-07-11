#!/usr/bin/python3


"""
Module: 101-stats.py

A module that reads stdin line by line
"""


import sys


def print_stats(total_size, status_codes):
    """
    Prints the statistics based on the accumulated metric

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary
    """
    print(f"File size: {total_size}")
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        count = status_codes[code]
        print(f"{code}: {count}")


def process_logs():
    """
    Processes the logs from stdin and computes metrics.

    Each 10 lines and after a keyboard interruption
    it prints the statistics since the beginning.
    """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            parts = line.strip().split(" ")
            if len(parts) >= 7:
                code = parts[-2]
                size = int(parts[-1])
                total_size += size

                if code in status_codes:
                    status_codes[code] += 1
                else:
                    status_codes[code] = 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    process_logs()
