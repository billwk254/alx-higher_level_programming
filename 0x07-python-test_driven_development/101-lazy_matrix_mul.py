#!/usr/bin/python3


"""
Lazy Matrix Multiplication

This module provides a function to multiply two matrices using the NumPy module.

"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): Matrix A represented as a list of lists.
        m_b (list): Matrix B represented as a list of lists.

    Returns:
        numpy.ndarray: Resultant matrix after multiplying matrix A and matrix B.

    Raises:
        ValueError: If m_a or m_b is not a valid matrix or m_a and m_b cannot be multiplied.

    Example:
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        array([[ 7, 10],
               [15, 22]])

        >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        array([[13, 16]])

    """

    try:
        matrix_a = np.array(m_a)
        matrix_b = np.array(m_b)
        result = np.matmul(matrix_a, matrix_b)
        return result.tolist()
    except ValueError as err:
        raise ValueError("m_a and m_b can't be multiplied") from err
