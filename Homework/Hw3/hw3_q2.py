# input
num_rows = int(input("Please enter a positive integer: "))

# WHILE
# variables
current_num1 = 1

# pre-print
print("Executing while-loop...")

# while-loop
while current_num1 <= (2 * num_rows):
    if current_num1 % 2 == 1:
        print(current_num1)
    
    current_num1 += 1

# separate the loops
print(" ")

# FOR
# pre-print
print("Executing for-loop...")

# for-loop
for num in range(2 * num_rows):
    if num % 2 == 1:
        print(num)
        
    num += 1
