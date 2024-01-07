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
