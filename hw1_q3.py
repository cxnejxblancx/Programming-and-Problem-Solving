"""
Author: Malani Snowden
Assignment / Part: HW1 - Q3
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# pre-print
print("Please enter number of coins:")

# input
user_quarters = int(input("Number of quarters: "))
user_dimes = int(input("Number of dimes: "))
user_nickels = int(input("Number of nickels: "))
user_pennies = int(input("Number of pennies: "))

# constants
pennies_in_dollar = 100
pennies_in_quarter = 25
pennies_in_dime = 10
pennies_in_nickel = 5

# conversions
pennies_in_user_quarters = (user_quarters * pennies_in_quarter)
pennies_in_user_dimes = (user_dimes * pennies_in_dime)
pennies_in_user_nickels = (user_nickels * pennies_in_nickel)
user_total_in_pennies = (pennies_in_user_quarters + pennies_in_user_dimes + pennies_in_user_nickels + user_pennies)

total_user_dollars = (user_total_in_pennies // pennies_in_dollar)
total_user_cents = ((user_total_in_pennies % pennies_in_dollar))

# print
print("The total is " + str(total_user_dollars) + " dollar(s) and " + str(total_user_cents) + " cent(s)")