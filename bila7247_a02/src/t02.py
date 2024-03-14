"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-29"
-------------------------------------------------------
"""
# Imports

# Constants

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
num = int(input("Enter a positive two-digit integer: "))
if 10 <= num <= 99:

    tens_digit = num // 10
    ones_digit = num % 10

    difference = tens_digit - ones_digit
    print(f"The difference of the digits of ", num, " is ", difference)
