"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports
import random
import string
# Constants
matrix = []


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    if value_type == 'float':
        generate = random.uniform
    elif value_type == 'int':
        generate = random.randint
    else:
        generate = None
    if generate is not None:
        matrix = [[generate(low, high) for _ in range(cols)]
                  for _ in range(rows)]
        return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    if not(isinstance(rows, int) and isinstance(cols, int) and rows > 0 and cols > 0):
        matrix = "This matrix is incorrect"

    matrix = [[random.choice('abcdefghijklmnopqrstuvwxyz')
               for i in range(cols)] for i in range(rows)]

    return matrix


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    word_length = len(word_list[0])
    if any(len(word) != word_length for word in word_list):
        raise ValueError("All words in the list must have the same length")

    matrix = [list(word) for word in word_list]

    return matrix


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """

    rows = len(matrix)
    cols = len(matrix[0])

    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0

    for i in range(rows):
        for j in range(cols):
            current_value = matrix[i][j]

            if current_value < smallest:
                smallest = current_value
            if current_value > largest:
                largest = current_value

            total += current_value

    average = total / (rows * cols)

    return smallest, largest, total, average


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= num

    return


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])
    print("    ", end="")
    for col in range(cols):
        print(f"{col:4}", end="")
    print()
    for row in range(rows):
        print(f"{row:2}  ", end="")
        for col in range(cols):
            print(f"{matrix[row][col]:4}", end="")
        print()
    return
