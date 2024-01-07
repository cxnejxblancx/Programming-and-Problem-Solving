def problem2():
    outer_limit = 5
    for outer_var in range(2, outer_limit):
        inner_var = 100
        while inner_var > 10:
            print("inner: ", inner_var)
            inner_var //= outer_var
        print(inner_var)


def problem3():
    test_str = "New York"
    test_int = 42
    first = True
    second = False

    print(not (first or second))
    print(test_int >= 41 and not second and first)
    print(1 <= test_int % 2)
    print(test_str < "New Jersey")
    print(first or second and test_int > 100)
    print(test_str < "new york")
    print("java" > "python")


def problem4_1():
    # input
    num = int(input("Enter a value: "))

    # for-loop
    for base in range (1, (num)): 
        for power in range(1, (num + 1)):
            if base ** power == num:
                print("Base found: " + str(base))


def problem4_2():
    # input
    value = int(input("Enter a value: "))

    # for-loop --> base
    for base in range(2, value):
        # nested for-loop --> power
        for power in range(1, (value + 1)):
            if base ** power == value:
                print("Base found: " + str(base))


def problem5_1():
    # input
    pay_rate = float(input("pay rate? "))
    first_start = float(input("start of first shift? "))
    first_end = float(input("end of first shift? "))
    second_start = float(input("start of second shift? "))

    # variables
    total_hrs = 0
    hrs_between = 0
    total_pay = 0
    min_wage = 15
    overtime_pay_rate = pay_rate * 1.5
    overtime_hours = 0

    # conditionals
    if second_start == 0:
        total_hrs = (first_end - first_start)

        if total_hrs > 10:
            total_pay += min_wage

    elif second_start > 0:
        second_end = float(input("end of second shift? "))
        total_hrs = (first_end - first_start) + (second_end - second_start)
        hrs_between = second_start - first_end

        if hrs_between > 1:
            total_pay += min_wage 

        elif second_end - first_start > 10:
            total_pay += min_wage
    
    # adjust variables
    if total_hrs > 8:
        overtime_hours = (total_hrs - 8)
        total_pay += (overtime_hours * overtime_pay_rate)
        total_hrs = 8

    total_pay += (total_hrs * pay_rate)
    total_pay = round(total_pay, 2)

    # final print
    print("Total Pay: $" + str(total_pay))


def problem5_2():
    # inputs
    pay_rate = float(input("pay rate? "))
    start_first = float(input("start of first shift? "))
    end_first = float(input("end of first shift? "))
    start_second = float(input("start of second shift? "))

    # variables
    workday_hrs = 0
    total_pay = 0

    # conditionals
    if start_second != 0: # 2 shifts
        end_second = float(input("end of second shift? "))
        workday_hrs = (end_first - start_first) + (end_second - start_second)
        if (start_second - end_first) > 1: # SPLIT SHIFT
            total_pay += 15
        elif (end_second - start_first) > 10: # SPREAD OF HOURS
            total_pay += 15

    else: # 1 shift
        workday_hrs = (end_first - start_first)
        if workday_hrs > 10: # SPREAD OF HOURS
            total_pay += 15

    if workday_hrs > 8: # OVERTIME
        total_pay += (((workday_hrs - 8) * (pay_rate * 1.5)) + (8 * pay_rate))
    
    else:
        total_pay += (workday_hrs * pay_rate)
    
    # adjust total_pay variable
    total_pay = round(total_pay, 2)

    # final print
    print("Total Pay: $" + str(total_pay))

problem5_2()
