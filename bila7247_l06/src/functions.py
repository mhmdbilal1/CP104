"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-10-25"
-------------------------------------------------------
"""
# Imports

# Constants


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(2, num+1, 2):
        total = total + i
    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(height):
        for j in range(width):
            print(char, end='')
        print()

    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(n, 2, -1):

        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(
            f"Take one down, pass it around, {i-1} {'bottles' if i-1 > 1 else 'bottle'} of beer on the wall.")
        print("--")
    print("2 bottles of beer on the wall, 2 bottles of beer.")
    print("Take one down, pass it around, 1 bottle of beer on the wall.")
    print("--")
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall!")
    print("--")
    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    if burnt_per_minute <= 0 or start <= 0 or end < start or inc <= 0:
        print("Invalid input. Please enter valid values.")
        return

    print("Time (minutes) \t Calories Burnt")
    print("---------------------------------")

    for current_time in range(start, end + 1, inc):
        calories_burnt = burnt_per_minute * current_time
        print(f"{current_time} \t\t\t {calories_burnt}")


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    minimum = float('inf')  # Set to positive infinity initially
    maximum = float('-inf')  # Set to negative infinity initially
    total = 0.0

    # Ask the user to input n values
    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))

        # Update minimum and maximum
        minimum = min(minimum, value)
        maximum = max(maximum, value)

        # Update total
        total += value

    # Calculate average
    average = total / n
    return(minimum, maximum, total, average)
