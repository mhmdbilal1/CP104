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
from functions import customer_append
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
    # Open the file for appending
    with open("customers.txt", "a") as file_handle:
        # Sample data to append
        data_to_append = ['35612', 'David', 'Brown', 237.56, '2008-10-10']

        # Call the function to append the data to the file
        customer_append(file_handle, data_to_append)

    print("Data appended to file.")
