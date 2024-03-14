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
from functions import line_numbering
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


with open("wilde.txt", "r", encoding="utf-8") as fh_read:
    with open("wilde_numbered.txt", "w", encoding="utf-8") as fh_write:
        print(line_numbering(fh_read, fh_write))
