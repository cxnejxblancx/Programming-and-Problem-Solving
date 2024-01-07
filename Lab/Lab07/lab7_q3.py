# input
message = input("Please enter your  message: ")

# variables
upper_message = message.upper()
num_vowels = 0
num_a = 0
num_e = 0
num_i = 0
num_o = 0
num_u = 0

# conditionals
for char in upper_message:
    num_a = upper_message.count("A")
    num_e = upper_message.count("E")
    num_i = upper_message.count("I")
    num_o = upper_message.count("O")
    num_u = upper_message.count("U")
    num_vowels = num_a + num_e + num_i + num_o + num_u

# final print
print("Total number of vowels: " + str(num_vowels))
