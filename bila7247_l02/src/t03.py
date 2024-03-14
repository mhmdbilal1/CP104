"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-17"
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

lDogs = int(input('Enter the number of large dogs groomed'))
sDogs = int(input('Enter the number of large dogs groomed'))
LDOGCOST = 75
SDOGCOST = 50
moneyMade = lDogs*LDOGCOST + sDogs*SDOGCOST
print('Total earned for the day:', moneyMade)
