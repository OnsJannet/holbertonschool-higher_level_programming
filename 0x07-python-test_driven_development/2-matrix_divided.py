#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    matrix_divided - divide a matrix
    @matrix: where Type matrix must be a (list of lists) of integers/floats
    @div: where Type div must must be a number
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    new = []
    for row in matrix:
        sub = []
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for i in range(len(row)):
            if type(row) != list:
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')
            if type(matrix) != list:
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')
            if len(matrix) == 0:
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')
            sub.append(round((row[i] / div), 2))
        new.append(sub)
    return new
