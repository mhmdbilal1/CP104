"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-09-30"
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

foundationLength = float(input("Foundation length (m): "))
foundationWidth = float(input("Foundation width  (m): "))
foundationHeight = float(input("Foundation height (m): "))
wallheight = float(input("Wall height       (m): "))
costOfConcrete = float(input("Cost of concrete ($/m^3): "))
costOfBricks = float(input("Cost of bricks ($/m^2): "))
foundationArea = foundationLength*foundationWidth*foundationHeight
bricksNeeded = (2*(wallheight*foundationLength) +
                2*(wallheight*foundationWidth))
print('Concrete needed for foundation (m^3): ', foundationArea)
print('Cost of concrete: $', costOfConcrete * foundationArea)
print('Bricks needed for walls (m^2): ', bricksNeeded)
print('Cost of bricks: $', bricksNeeded*costOfBricks)
print('Total cost: $', (bricksNeeded*costOfBricks) +
      (costOfConcrete * foundationArea))
