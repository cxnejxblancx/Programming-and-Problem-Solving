# input
user_num = int(input("Enter a decimal integer less than 100: "))

# calculations and conversions
L = "L" * (user_num // 50)
X = "X" * ((user_num % 50) // 10)
V = "V" * (((user_num % 50) % 10) // 5)
I = "I" * (((user_num % 50) % 10) % 5)

num_as_roman_numeral = ((L) + (X) + (V) + (I))

# print
print(num_as_roman_numeral)
