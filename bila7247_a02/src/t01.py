"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-23"
-------------------------------------------------------
"""
# Imports

# Constants
#
# def func():
#     """
#     -------------------------------------------------------
#     description
#     Use:
#     -------------------------------------------------------
#     Parameters:
#         name - description (type)
#     Returns:
#         name - description (type)
#     ------------------------------------------------------
#     """

tSales = int(input('Enter the total sales: $'))
print('Total sales:   $', tSales)
ATAX = float(18.5)
print('Annual tax:', ATAX)
print('Tax:           $', tSales*ATAX/100)
