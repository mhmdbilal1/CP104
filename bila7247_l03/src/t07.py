"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-26"
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
breakfast = float(input("Enter cost of breakfast: $"))
lunch = float(input("Enter cost of lunch: $"))
supper = float(input("Enter cost of supper: $"))

total = breakfast+lunch+supper

print("Meal         Cost")
print(f"Breakfast    ${breakfast:7.2f}")
print(f"Lunch        ${lunch:7.2f}")
print(f"Supper       ${supper:7.2f}")
print(f"Total        ${total:7.2f}")
