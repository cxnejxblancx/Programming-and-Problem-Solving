# input
user_input = int(input("Enter a positive integer: "))

# for-loop --> check each number from 1 to user_input (inclusive on both ends)
for num in range(1, (user_input + 1)):
    # variables
    num_odds = 0 # keep count of the number of ODD digits within the user input
    num_evens = 0 # keep count of the number fo EVEN digits within the user input
    digit = num # set the digits equal to the number of each iteration

    # while-loop --> control what happens when the number is not a single digit variable 
    while digit >= 10:
        # conditionals --> control which digits within the user inputted number are selected
        if (digit == 10) or (digit % 10 == 0):
            if (digit > 0) and (digit % 2 != 0):
                num_odds += 1

        elif (digit % 10) % 2 == 0:
            num_evens += 1

        else:
            num_odds += 1

        # replace digit value with the result of the previous digit floor divided by 10
        digit = digit // 10

    # conditionals --> control which variable is adjusted
    if digit % 2 == 0: # if the digit is even, add to the even digit counter
        num_evens += 1

    elif digit % 2 > 0: # can't be an even number# if the digit is odd, add to the odd digit counter
        num_odds += 1

    # conditional --> control which numbers within the range of the user input are printed
    if num_evens > num_odds: # if the number contains more even than odd digits, print the number
        print(num, end = " ")
    
