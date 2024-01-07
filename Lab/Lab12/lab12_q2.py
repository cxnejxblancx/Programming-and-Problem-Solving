# variables
my_str = input("Enter a string: ")
length = len(my_str)

# list comprehension
chars_twice = [char for num in range(2) for char in my_str]

# final print
print(chars_twice)
