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

flyers = int(input('Number of flyers:'))

noOfPeople = int(input('Number of flyers:'))

flyersPerPerson = int(flyers/noOfPeople)
flyersLeftOver = int(flyers % noOfPeople)
print("Flyers per delivery person: ", flyersPerPerson)
print("Flyers left over: ", flyersLeftOver)
