"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
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
BASE_FOR_COST = 125
COST_PER_EXTRA_SERVICE = 25
DISCOUNT = 0.10
# your constants here


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌‌​​​‌​‌‌​‌​‌​‌:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    question_extra_service = int(
        input("How many extra services are you purchasing? "))

    user_vip = input("Are you a VIP member (Y/N)? ")

    cost = BASE_FOR_COST + (question_extra_service * COST_PER_EXTRA_SERVICE)

    if question_extra_service > 1 and user_vip == "Y":
        total_pay = cost * DISCOUNT
        cost = cost - total_pay

    return
