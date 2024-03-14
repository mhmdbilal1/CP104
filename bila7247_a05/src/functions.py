"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-11-04"
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


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    if number > 0:
        product = 1
    for i in range(1, number + 1):
        product *= i

    return product


def calories_treadmill(per_min, minutes):
    """
    Calculates the number of calories burned every five minutes given the number of calories burned per minute (per_min) an the total number of minutes run (minutes).
    Use: calories_treadmill (per min, minutes)
    Parameters:
    per_min - number of calories burned per minute (float)
    minutes - total number of minutes run (float)
    Returns:
    None
    -----------------------------------------------------------------
    """

    print(f"{'Time':<7} | {'Calories Burned':<15}")
    print("-------------------------------------")

    # Loop to print results every five minutes
    for time_elapsed in range(5, minutes + 1, 5):
        calories_burned = per_min * time_elapsed
        print(f"{time_elapsed} min  |  {calories_burned:.1f}")
    return


def arrow_up(rows):
    """
    Draw an arrow pointing up using '#' characters.
    Use: arrow_up(rows)
    Parameters:
    - rows (int): The number of rows in the arrow.
    Returns:
    None.
    """
    for i in range(rows):
        # Print spaces before the first '#'
        for j in range(rows - i - 1):
            print(" ", end="")

        # Print the first '#'
        print("#", end="")

        # Print spaces between '#' characters
        for k in range(2 * i - 1):
            print(" " if i > 0 else "", end="")

        # Print additional '#' if not the top row
        if i > 0:
            print("#", end="")

        # Move to the next line for the next row
        print()
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("", end="\t")
    for i in range(start_num, stop_num + 1):
        print(f"{i}\t", end="")
    print("\n", end="")

    # Print the separator line
    print("   " + "-" * (8 * (stop_num - start_num + 1)))

    # Print the multiplication table
    for i in range(start_num, stop_num + 1):
        print(f"{i} |", end="\t")
        for j in range(start_num, stop_num + 1):
            print(f"{i * j}\t", end="")
        print("")
    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total += start
        start += increment
    return total
