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
location1 = "left"
location2 = "middle"
location3 = "right"

# Define the width of each line
line_width = 20

# Print the values with the specified formatting
print(f"{location1:-<{line_width}}")
print(f"{location2:-^{line_width}}")
print(f"{location3:->{line_width}}")
