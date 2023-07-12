#!/usr/bin/python3


"""
Module: pascal_triangle
Description: This module defines the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Generates the Pascal's triangle of n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing the Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
