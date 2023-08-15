#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in range(len(matrix)):
        for element_2 in range(len(matrix[element])):
            if element_2 != 0:
                print(" ", end='')
            print("{:d}".format(matrix[element][element_2]), end='')
        print()
