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
from functions import file_copy
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


fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("new_words.txt", "w", encoding="utf-8")
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()

print(f"Copying 'words.txt' to 'new_words.txt'")
