"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """

    # Generate a random number between 1 and high
    target_number = randint(1, high)

    # Initialize the number of guesses made by the user
    count = 0

    # Start the game loop
    while True:
        # Ask the user to guess the number
        user_guess = int(input(f"Guess the number between 1 and {high}: "))
        count += 1

        # Check if the guess is correct, too low, or too high
        if user_guess == target_number:
            print(
                f"Congratulations! You guessed the number in {count} attempts.")
            break
        elif user_guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    # Return the number of guesses
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    if target < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Special case for 0
    if target == 0:
        power = 1

    # Initialize power to 1
    power = 1

    # Keep doubling the power until it's greater than or equal to the target
    while power < target:
        power *= 2

    return power


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    if target < 0:
        raise ValueError("Target value must be greater than or equal to 0")

    current_sum = 0
    current_number = 1
    while True:
        current_sum += current_number ** 2

        if current_sum >= target:
            return current_sum

        current_number += 1


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0.0
    l_total = 0.0
    s_total = 0.0
    a_total = 0.0

    # Variable to track whether the user wants to enter data for another day
    another_day = True

    while another_day:
        # Get costs for each meal for the current day
        b_cost = float(input("Enter cost of breakfast for the day: "))
        l_cost = float(input("Enter cost of lunch for the day: "))
        s_cost = float(input("Enter cost of supper for the day: "))

        # Update total costs for each meal category and overall cost
        b_total += b_cost
        l_total += l_cost
        s_total += s_cost
        a_total += (b_cost + l_cost + s_cost)

        # Ask if the user wants to enter data for another day
        another_day_input = input(
            "Do you want to enter data for another day? (y for yes/n for no): ")
        another_day = another_day_input.lower() == 'y'

    # Return the calculated total costs
    return b_total, l_total, s_total, a_total


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    TOTAL = 0.0
    COUNT = 0
    TAX_RATE = 0.03625

    while True:

        employee_id = int(input("Enter employee ID number (enter 0 to end): "))

        if employee_id == 0:
            break

        HOURLY_RATE = float(input("Enter hourly wage rate: "))
        OVERTIME_RATE = 1.5*HOURLY_RATE
        hours_worked = float(
            input("Enter number of hours worked during the week: "))

        if hours_worked > 40:
            OVERTIME_HOURS = hours_worked - 40
            gross_salary = 40 * HOURLY_RATE + OVERTIME_HOURS * OVERTIME_RATE
        else:
            gross_salary = hours_worked * HOURLY_RATE

        net_salary = gross_salary * (1 - TAX_RATE)

        TOTAL += net_salary
        COUNT += 1

    if COUNT == 0:
        AVERAGE = 0.0
    else:
        AVERAGE = TOTAL / COUNT

    return TOTAL, AVERAGE
