#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx_stack = []
    for element in matrix:
        mtx_stack.append(list(map(lambda element: element**2, element)))
    return (mtx_stack)
