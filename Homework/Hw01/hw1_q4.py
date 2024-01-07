# pre-print
print("Please enter your amount of dollars and cents, in two separate lines.")

# input
user_dollars = int(input())
user_cents = int(input())

# constants
pennies_in_dollar = 100
pennies_in_quarter = 25
pennies_in_dime = 10
pennies_in_nickel = 5

# conversions and calculations
user_total_in_pennies = (user_dollars * pennies_in_dollar) + user_cents

quarters_in_user_total = (user_total_in_pennies // pennies_in_quarter)
dimes_in_user_total = ((user_total_in_pennies % pennies_in_quarter) // pennies_in_dime)
nickels_in_user_total = (((user_total_in_pennies % pennies_in_quarter) % pennies_in_dime) // pennies_in_nickel)
pennies_remaining_in_user_total = (((user_total_in_pennies % pennies_in_quarter) % pennies_in_dime) % pennies_in_nickel)

# print
print(str(user_dollars) + " dollars and " + str(user_cents) + " cents are: " + str(quarters_in_user_total) + " quarters, " + str(dimes_in_user_total) + " dimes, " + str(nickels_in_user_total) + " nickels and " + str(pennies_remaining_in_user_total) + " pennies")
