"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Muhammad Bilal
ID:     169047247
Email:  bila7247@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants

# your constants here


# Constants
loonies_division = 100
quarters_division = 25
dimes_division = 10
nickels_division = 5
# your constants here


def minimal_change(cents):
    """
    -------------------------------------------------------
    Breaks down cents into a minimal number of coins.
    The change can be:
        loonies - coins worth 100 cents
        quarters - coins worth 25 cents
        dimes - coins worth 10 cents
        nickels - coins worth 5 cents
    Use: loonies, quarters, dimes, nickels = minimal_change(cents)
    -------------------------------------------------------
    Parameters:
        cents - number of cents (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌‌‌​​​‌​‌‌​‌​‌​‌:
        loonies - number of loonies ($1 coins) (int)
        quarters - number of quarters (25 cent coins) (int)
        dimes - number of dimes (10 cent coins) (int)
        nickels - number of nickels (5 cent coins) (int)
    -------------------------------------------------------
    """

    # your code here
    loonies = cents // loonies_division
    cents = cents % loonies_division

    quarters = cents // quarters_division
    cents = cents % quarters_division

    dimes = cents // dimes_division
    cents = cents % dimes_division

    nickels = cents // nickels_division
    cents = cents % nickels_division

    return loonies, quarters, dimes, nickels
