"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-25"
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
Principal_Amount = float(input('Enter the principle amount'))
Interest_Rate = float((input("Enter rate of interest")))
Interest_Compounded_Per_Year = int(input("Number of years"))
n = int(input('How many times is interest compounded in a year'))
# A = P*(1+((r/100)/n))**(n*t)

A = Principal_Amount*(1+((Interest_Rate/100)/n))**(n *
                                                   Interest_Compounded_Per_Year)
# Result_A = Principal_Amount * (1+((Interest_Rate/100)/Interest_Compounded_Per_Year))**(Interest_Compounded_Per_Year*n)
print('Balance: $ ', A)
