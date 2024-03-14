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
from functions import count_frequency_word
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


word = "Exercise"
fh = open('words.txt', "r", encoding="utf-8")
numbers = count_frequency_word(fh, word)
fh.close()
print(f'Word to count:{word}')
print(f"'{word}' appears {numbers} time(s)")
