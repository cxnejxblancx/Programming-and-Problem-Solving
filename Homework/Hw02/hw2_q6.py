# since you can assume the user will always enter valid inputs:
#   - invalid times such as 1290 or 2452 do not have to be accounted for
#   - ivalid dates such as "mon", "tue", etc. do not have to be accounted for

# NOTES
    # call in range [530 - 2100] --> Mon - Thr --> $0.55/min
    # call start < 530 or call start > 2100 --> mon - thr --> $0.35/min
    # any call --> Fri, Sat, Sun --> $0.10/min

# inputs
call_start_day = input("Enter the day the call started at: ")
call_start_time = int(input("Enter the time the call started at (hhmm): "))
call_duration = int(input("Enter the duration of the call (in minutes): "))

# conditionals
if (call_start_day == "Mon") or (call_start_day == "Tue") or (call_start_day == "Wed") or (call_start_day == "Thr"):
    if 530 <= call_start_time <= 2100:
        call_cost = round((call_duration * 0.55), 2)
        
    else: # the only other value the call_start_time could be is before 5:30am (530) or after 9pm (2100) now, so it does not need to be specififed
        call_cost = round((call_duration * 0.35), 2)

else: # since you can assume the user will always enter valid inputs, Fri, Sat, and Sun do not need to be specified here
    call_cost = round((call_duration * 0.1), 2)

# final print
print("This call will cost $" + str(call_cost))
