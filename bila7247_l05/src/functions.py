"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-10-19"
-------------------------------------------------------
"""
# Imports

# Constants
FULLTIME_10 = 1.05
FULLTIME_4 = 1.015
PART_10 = 1.03
PART_4 = 1.01
ALL = 1.02
CHILD_TICKET_AGE = 12
ADULT_TICKET_AGE = 18
SENIOR_TICKET_AGE = 60

RAISE_PERCENTAGE = 0.05
FULLTIME_10 = 1.05
FULLTIME_4 = 1.015
PART_10 = 1.03
PART_4 = 1.01
ALL = 1.02
YEAR_MAX = 10
YEAR_MIN = 4
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


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    magic_dt = day*month
    if magic_dt == year:
        magic_dt = True
    else:
        magic_dt = False

    return magic_dt


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """

    distance_v1 = abs(target - v1)
    distance_v2 = abs(target - v2)
    num = 0
    if distance_v1 <= distance_v2:
        num = v1
    else:
        num = v2

    return num


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    num = 0

    if 1 <= n <= 10:
        roman_numerals = ['I', 'II', 'III', 'IV',
                          'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        num = roman_numerals[n - 1]
    else:
        num = None
    return num


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """

    if status == "F":
        if years >= YEAR_MAX:
            new_salary = salary * (1 + RAISE_PERCENTAGE)
        elif years < YEAR_MIN:
            new_salary = salary * FULLTIME_4
        else:
            new_salary = salary * ALL

    elif status == "P":
        if years >= YEAR_MAX:
            new_salary = salary * PART_10
        elif years < YEAR_MIN:
            new_salary = salary * PART_4
        else:
            new_salary = salary * ALL

    return new_salary


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    AGE = int(input("Enter your age: "))
    INFANT = 0.00
    SENIOR = 4.00
    STUDENT = 3.00
    STUDENT_SCHOOL = 1.00
    ADULT = 5.00
    KIDS = 2.00
    INFANT_MIN = 3
    KID_MIN = 10
    ADULT_MIN = 18
    SENIOR_MIN = 65

    if AGE < INFANT_MIN:
        PRICE = INFANT
    elif INFANT_MIN <= AGE < KID_MIN:
        PRICE = KIDS
    elif KID_MIN <= AGE < ADULT_MIN:
        IS_STUDENT = input("Are you a student at the school? (Y/N): ")
        if IS_STUDENT == "Y":
            PRICE = STUDENT_SCHOOL
        else:
            PRICE = STUDENT
    elif ADULT_MIN <= AGE < SENIOR_MIN:
        PRICE = ADULT
    elif AGE >= SENIOR_MIN:
        PRICE = SENIOR
    else:
        PRICE = STUDENT

    print(f"The ticket price is: ${PRICE:.2f}")
    return PRICE
