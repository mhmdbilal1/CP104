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


UpperBMISAsia = 23
UpperBMISChina = 25
UpperBMI = 23

userHeightM = float(input('Enter your height (m):'))
userHeightM2 = userHeightM**2


userWeightKg = float(input('Enter you weight(Kg):'))

upperLimitBMI = int(input(
    'Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else):'))

# BMI: user mass (kg) / user height (m)^2
BMI = userWeightKg/userHeightM2

# BMI': user BMI / user BMI upper limit

BMIPrime = BMI/upperLimitBMI


print('Body Mass Index (kg/m^2) = ', BMI)
print('BMI Prime = ', BMIPrime)

# BMIPrimeSAsia = BMI / UpperBMISAsia
# BMIPrimeSChina = BMI / UpperBMISChina
# BMIPrime = (BMI/UpperBMI)
# print('Body Mass Index (kg/m^2)       is=', BMI)
# print('BMI Prime for South East Asian is:', BMIPrimeSAsia)
# print('BMI Prime for South China      is:', BMIPrimeSChina)
