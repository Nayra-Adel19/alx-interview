#!/usr/bin/python3
""" write a method that calculates the fewest number of operations """


def minOperations(n):
    """ write a method that calculates the fewest number of operations """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 0

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 2
        else:
            operations += 1

        current_length += clipboard

    return operations
