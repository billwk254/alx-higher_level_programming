#!/usr/bin/python3


"""
A module for a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list): Matrix A represented as a list of lists.
        m_b (list): Matrix B represented as a list of lists.

    Returns:
        list: Resultant matrix after multiplying matrix A and matrix B.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or an element is not an integer or float.
        ValueError: If m_a or m_b is empty, or m_a and m_b cannot be multiplied, or the matrices are not rectangles.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
