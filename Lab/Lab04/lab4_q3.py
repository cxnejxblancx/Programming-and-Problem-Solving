# input
iterations = int(input("Please enter a number: "))

# variables
result1 = 1
result2 = 1
fibonacci = 0

# for-loop
for i in range(iterations):
    # conditionals
    if i == 0:
        fibonacci = result1
        print(fibonacci)
    elif i == 1:
        fibonacci = result2
        print(fibonacci)
    else:
        fibonacci = result1 + result2
        print(fibonacci)
        
        # adjust variables
        result1 = result2
        result2 = fibonacci
    
    # adjust variable
    i += 1
