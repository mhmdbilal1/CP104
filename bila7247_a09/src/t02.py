"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-11-28"
-------------------------------------------------------
"""
# Imports
from functions import read_integers
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


file_handle = open("numbers.txt", "r", encoding="utf-8")
result_list = read_integers(file_handle)
print(result_list)

file_handle.close()
