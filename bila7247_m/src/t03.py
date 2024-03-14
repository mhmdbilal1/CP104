"""
-------------------------------------------------------
Midterm B Task 3 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
from t03_functions import servicing

cost = servicing()
COST = int(cost)
# Check if cost is not None before formatting
print(f"Cost: ${COST:.2f}")
