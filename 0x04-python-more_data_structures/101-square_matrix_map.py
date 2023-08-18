#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda az_row_: list(map(lambda element: element**2, az_row_)), matrix))
