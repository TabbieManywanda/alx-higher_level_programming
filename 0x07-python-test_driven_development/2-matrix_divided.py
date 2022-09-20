#!/usr/bin/python3
"""Defining a function that divides all elements
of a matrix
"""


def matrix_divided(matrix, div):
    """returns a new matrix having divided values"""
    size = None
    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for lst in matrix:
        if type(lst) is not list:
            raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(lst)
        elif size != len(lst):
            raise TypeError("Each row of the matrix must have the same size")
        for num in lst:
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round((num / div), 2) for num in lst] for lst in matrix]
