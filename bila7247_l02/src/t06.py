"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-20"
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
principle = float(input('Enter principle amount'))
years = int(input('years?'))
interest = float(input('interest rate'))
monthlyInterest = (interest/12)/100
months = years*12
monthly = principle*(monthlyInterest*(1+monthlyInterest) **
                     months)/((1+monthlyInterest) ** months-1)
print('The monthly payments are: $', monthly)
