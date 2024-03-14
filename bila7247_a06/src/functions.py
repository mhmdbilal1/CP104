"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-11-11"
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


def total_wins():
    """
    Asks the user to enter a series of strings representing the output of a game.
    The function returns a tuple containing two numbers:
    - The count of occurrences of the string "purple" in the input.
    - The count of occurrences of the string "gold" in the input.
    Returns:
        total_wins:(purple,gold)
    The function uses a while loop to continue accepting input until an empty string is entered.
    """
    purple_count = 0
    gold_count = 0
    while True:
        team = input("Enter the winning team: ")

        if not team:
            break
        if team.lower() == "purple":
            purple_count += 1
        elif team.lower() == "gold":
            gold_count += 1

    return purple_count, gold_count


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    if number <= 1:
        output = False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            output = False
        divisor += 1
        output = True

    return output


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    monthly_interest_rate = interest_rate / 100 / 12
    month = 1
    balance = principal_amount

    # Print header
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month  Interest   Payment   Balance")
    print("----------------------------------")

    while balance > 0:
        monthly_interest = balance * monthly_interest_rate

        actual_payment = min(payment, balance + monthly_interest)

        balance -= actual_payment - monthly_interest
        print(
            f"   {month:<3d}    {monthly_interest:.2f}    {actual_payment:.2f}    {balance:.2f}")
        month += 1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    num = abs(number)

    while num > 0:
        num = num // 10
        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1
    return total
