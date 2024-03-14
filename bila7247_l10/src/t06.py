"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-11-23"
-------------------------------------------------------
"""
# Imports
from functions import number_stats
# Constants


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


if __name__ == "__main__":
    with open("numbers.txt", "r") as file_handle:
        smallest, largest, total, average = number_stats(file_handle)
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
