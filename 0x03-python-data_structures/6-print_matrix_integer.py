#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        print(" ".join("{:d}".format(w) for w in x))
