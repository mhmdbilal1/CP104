"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from functions import customer_record
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
    with open("customers.txt", "r") as file_handle:
        record_number = int(input("Enter a record number: "))
        result = customer_record(file_handle, record_number)
print(result)
