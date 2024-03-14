"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-18"
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

NoOfFlyers = int(input("Enter number of flyers"))
NoOfVolunteers = int(input("Enter number of volunteers"))
flyersPerVolunteer = NoOfFlyers//NoOfVolunteers
flyersLeftOver = NoOfFlyers % NoOfVolunteers
print('Flyers per volunteer:', flyersPerVolunteer)
print('Flyers left over:', flyersLeftOver)
