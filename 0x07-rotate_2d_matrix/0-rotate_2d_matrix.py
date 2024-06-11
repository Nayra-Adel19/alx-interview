#!/usr/bin/python3
""" Rotate the given 2D matrix 90 degrees clockwise in-place """


def rotate_2d_matrix(matrix):
    """
    Rotate the given 2D matrix 90 degrees clockwise in-place.
    :param matrix: List of lists representing the 2D matrix.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
