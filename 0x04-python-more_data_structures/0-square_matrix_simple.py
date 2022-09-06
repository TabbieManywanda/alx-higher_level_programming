#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []

    for x in matrix:
        newmatrix.append(list(map(lambda i: i**2, x)))
    return newmatrix
