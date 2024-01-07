def calculate_income(hourly_rate):
    """
    Calculate weekly income based on hourly rate and hours worked
    :param hourly_rate: the hourly pay rate used to calculate income
    :return: float of total_pay
    """
    # works 5 days/week
    # input whole number hours
    # hours > 40 --> overtime --> paid at 1.5x standard hourly rate

    # variables
    overtime_rate = 1.5 * hourly_rate
    total_hours = 0
    total_pay = 0

    # for-loop
    for iteration in range(5):
        day_hours = int(input("Enter the number of hours worked today: "))
        total_hours += day_hours

    # conditonals
    if total_hours > 40:
        overtime_hours = total_hours - 40
        total_pay = (40 * hourly_rate) + (overtime_hours * overtime_rate)

    else:
        total_pay = total_hours * hourly_rate

    # SEPARATE
    print()

    # return
    return float(total_pay)

def calculate_expenses():
    """
    Calculate weekly expenses based on user input of expenses
    :return: float of total expenses
    """

    # input
    money_spent = input("Enter how much money you spent of Q if done: ")

    # variable
    total_expenses = 0

    # while-loop
    while money_spent != "Q":
        total_expenses += float(money_spent)
        money_spent = input("Enter how much money you spent of Q if done: ")

    # SEPARATE
    print()

    # return
    return float(total_expenses)

def budget_outcome(income, expenses):
    """
    Determine whether the user had a gain or loss over the week.
    :param income: total amount of weekly income
    :param expenses: total weekly expenses
    :return: the difference between income and expenses
    """

    # calculation
    difference = income - expenses

    # conditionals
    if difference < 0:
        print(f"You had a loss of {difference}")
    
    elif difference > 0:
        print(f"Well done. You had a gain of {difference}")

    # return
    return difference

def main():
    # variables
    income = calculate_income(15)
    expenses = calculate_expenses()

    # call function
    budget_outcome(income, expenses)

main()
