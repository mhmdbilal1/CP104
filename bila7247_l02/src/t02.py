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
LBOUND = 32
farenheit = int(input('Enter temperature in farenheit'))
celcius = (farenheit-32)*5/9
if celcius == LBOUND:
    pass
print('Temperature (C):', celcius)
