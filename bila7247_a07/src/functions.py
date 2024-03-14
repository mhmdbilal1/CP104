"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports

# Constants
factors = []
minuend = []


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


def list_factors(number):
    """
    -------------------------------------------------------
    description
    Use: number to input the number
    -------------------------------------------------------
    Parameters:
        factors - to give al the possible factors
    Returns:
        list_factors(factors)
    ------------------------------------------------------
    """
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []

    while True:
        number = input("Enter a positive number (enter 0 to stop): ")
        if number == '0':
            break
        number = int(number)
        if number > 0:
            number_list.append(number)
        else:
            print("Error: Please enter a positive number.")
    print(number_list)
    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = [index for index, num in enumerate(numbers)
                  if num == target_number]
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    indexes_remove = []
    for i in range(len(minuend)):
        if minuend[i] in subtrahend:
            indexes_remove.append(i)
    for i in reversed(indexes_remove):
        minuend.pop(i)
    return


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            ans = False, i
            break
        else:
            ans = True, -1

    return ans
