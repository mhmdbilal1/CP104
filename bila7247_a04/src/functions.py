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
#     """
# hoo_rah takes an integer parameter and returns one of the following strings:
#
# "Hoo" if number is evenly divisible by 2
# "Rah" if number is evenly divisible by 7
# "Hoo Rah" if number is evenly divisible by both 2 and 7
# "Zip" if number is none of the above


def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    if day_num == 1:
        day = ("Sunday")
    elif day_num == 2:
        day = ("Monday")
    elif day_num == 3:
        day = ("Tuesday")
    elif day_num == 4:
        day = ("Wednesday")
    elif day_num == 5:
        day = ("Thursday")
    elif day_num == 6:
        day = "Friday"
    elif day_num == 7:
        day = "Saturday"
    else:
        day = "Error"

    return day


def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """

    if air_quality_index <= 50:
        pollution = "Good"
    elif air_quality_index <= 100:
        pollution = "Moderate"
    elif air_quality_index <= 150:
        pollution = "Unhealthy for Sensitive Groups"
    elif air_quality_index <= 200:
        pollution = "Unhealthy"
    elif air_quality_index <= 300:
        pollution = "Very Unhealthy"
    elif air_quality_index >= 300:
        pollution = "Hazardous"
    else:
        pollution = "Error"
    return pollution


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    if val1 >= val2 and val1 >= val3:
        if val2 >= val3:
            average = (val1 + val2) / 2
        else:
            average = (val1 + val3) / 2

    elif val2 >= val1 and val2 >= val3:
        if val1 >= val3:
            average = (val2 + val1) / 2
        else:
            average = (val2 + val3) / 2

    else:
        if val1 >= val2:
            average = (val3 + val1) / 2
        else:
            average = (val3 + val2) / 2

    return average


def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if (rgb_colour1 == "red" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "red"):
        rgb_colour = "fuchsia"

    elif (rgb_colour1 == "red" and rgb_colour2 == "green") or (rgb_colour1 == "green" and rgb_colour2 == "red"):
        rgb_colour = "yellow"

    elif (rgb_colour1 == "green" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "green"):
        rgb_colour = "aqua"

    elif (rgb_colour1 == "red" and rgb_colour2 == "red") or (rgb_colour1 == "red" and rgb_colour2 == "red"):
        rgb_colour = "red"

    elif (rgb_colour1 == "blue" and rgb_colour2 == "blue") or (rgb_colour1 == "blue" and rgb_colour2 == "blue"):
        rgb_colour = "blue"

    elif (rgb_colour1 == "green" and rgb_colour2 == "green") or (rgb_colour1 == "green" and rgb_colour2 == "green"):
        rgb_colour = "green"

    else:
        rgb_colour = "Error"

    return rgb_colour


def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    if not isinstance(width, int) or width <= 0:
        print("Width should be a positive integer.")
        return

    if not isinstance(char, str) or len(char) != 1:
        print("Char should be a single character.")
        return

    for i in range(width):
        for j in range(width):

            if i == 0 or i == width - 1 or j == 0 or j == i or j == width - 1:
                print(char, end=' ')
            else:
                print(' ', end=' ')
        print()


def hoo_rah(number):
    divisible_by_2 = (number // 2) * 2 == number
    divisible_by_7 = (number // 7) * 7 == number
    ans = 0

    if divisible_by_2 and divisible_by_7:
        ans = "Hoo Rah"
    elif divisible_by_2:
        ans = "Hoo"
    elif divisible_by_7:
        ans = "Rah"
    else:
        ans = "Zip"
    return ans
