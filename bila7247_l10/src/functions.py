"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Bilal
ID:      169047247
Email:   bila7247@mylaurier.ca
__updated__ = "2023-12-14"
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


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    fh.seek(0)

    lines = fh.read().strip().split('\n')
    return lines[n].split(',') if 0 <= n < len(lines) else []


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    match = next((line.strip().split(',')
                 for line in fh if line.strip().split(',')[0] == id_number), None)
    if match:
        result = match
    return result

# if value_type == 'float':
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 print(f"{matrix[i][j]:8.2f}", end="")
#             print()
#     elif value_type == 'int':
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 print(f"{matrix[i][j]:8}", end="")
#             print()
#     else:
#         print("Invalid value_type. Please use 'float' or 'int'.")


def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """

    best_customer = None
    max_balance = float('-inf')
    for line in fh:
        record = line.split(',')
        try:
            balance = float(record[1])
        except ValueError:
            continue

        if balance > max_balance:
            max_balance = balance
            best_customer = record

    return best_customer


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """

    record = ",".join(map(str, fields))
    fh.write(record + "\n")
    return


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    smallest = float('inf')
    largest = float('-inf')
    total = 0
    count = 0

    for line in fh:
        num = float(line.strip())
        count += 1
        total += num

        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    if count == 0:
        smallest = largest = total = average = 0.0
    else:
        average = total / count

    return int(smallest), int(largest), int(total), average


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    count = 0
    line = fh.readline()
    while line != '':
        if line.strip() == word:
            count += 1
        line = fh.readline()
    return count


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    line = fh_1.readline()
    while line != "":
        fh_2.write(line)
        line = fh_1.readline()
    return None
