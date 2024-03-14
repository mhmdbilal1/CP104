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
input_date_1 = int(input("Enter a date in the format YYYYMMDD: "))
year_1 = input_date_1 // 10000
month_1 = (input_date_1 % 10000) // 100
day_1 = input_date_1 % 100
formatted_date_1 = f"{year_1}/{month_1:02d}/{day_1:02d}"
print(f"The reformatted date: {formatted_date_1}")
