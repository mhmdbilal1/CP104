"""
-------------------------------------------------------
Midterm B Task 2 Function Definitions
-------------------------------------------------------
Author: Muhammad Bilal
ID:     169047247
Email:  bila7247@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""


def categorize(strokes):
    """
    -------------------------------------------------------
    Determines the golf skill rating given number of strokes to complete 18 holes.
        If strokes are 70 or less, the rating is "Grandmaster".
        If strokes are 85 or less, the rating is "Master".
        If strokes are 100 or less, the rating is "Professional".
        If strokes are greater than 100, the rating is "Amateur".
        If points is less than 0, return "Error"
    Must use a fallthrough algorithm.
    Use: rating = categorize(strokes)
    -------------------------------------------------------
    Parameters:
        strokes - strokes to complete 18 holes of golf (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​‌​​‌‌​​‌‌‌‌:
        category - description of skill rating (str)
    -------------------------------------------------------
    """

    # your code here
    # your code here
    if strokes < 0:
        rating = "Error"
    elif strokes <= 70:
        rating = "Grandmaster"
    elif strokes <= 85:
        rating = "Master"
    elif strokes <= 100:
        rating = "Professional"
    else:
        rating = "Amateur"

    return rating

    return
