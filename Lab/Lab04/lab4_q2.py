# pre-print
print("This is a four operation calculator.")

# input
will_continue = input("Hit enter to continue and Q to quit calculator: ")

# while-loop
while will_continue == "":
    # input
    first_num = float(input("Enter your first number: "))
    operator = input("Enter the operation (+, -, *, /): ")
    second_num = float(input("Enter your second number: "))

    # conditionals
    if (operator == "/") and (second_num == 0):
        print(str(first_num) + " " + operator + " " + str(second_num) + " is an invalid operation.")

    elif operator == "+":
        final_result = first_num + second_num
        print(str(first_num) + " " + operator + " " + str(second_num) + " = " +  str(final_result))

    elif operator == "-":
        final_result = first_num - second_num
        print(str(first_num) + " " + operator + " " + str(second_num) + " = " +  str(final_result))

    elif operator == "*":
        final_result = first_num * second_num
        print(str(first_num) + " " + operator + " " + str(second_num) + " = " +  str(final_result))

    elif operator == "/":
        final_result = first_num / second_num
        print(str(first_num) + " " + operator + " " + str(second_num) + " = " +  str(final_result))

    else:
        print( str(first_num) + " " + str(operator) + " " + str(second_num) +  " is an invalid operation.")

    # input
    will_continue = input("Hit enter to continue and Q to quit calculator: ")

# conditionals
if will_continue == "Q":
    print("Goodbye!")

else:
    print("Invalid input.")
  
