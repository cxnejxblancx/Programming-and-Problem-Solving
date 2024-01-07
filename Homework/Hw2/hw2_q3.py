# constants
MIN_IN_HOUR = 60
MIN_IN_DAY = 60 * 24

# inputs
semi_days = int(input("Please enter the number of days Semi has worked: "))
semi_hours = int(input("Please enter the number of hours Semi has worked: "))
semi_minutes = int(input("Please enter the number of minutes Semi has worked: "))
daniel_days = int(input("Please enter the number of days Daniel has worked: "))
daniel_hours = int(input("Please enter the number of hours Daniel has worked: "))
daniel_minutes = int(input("Please enter the number of minutes Daniel has worked: "))

# conversions
semi_daniel_days_in_min = ((semi_days + daniel_days) * (60 * 24))
semi_daniel_hours_in_min = ((semi_hours + daniel_hours) * (60))
semi_daniel_minutes = ((semi_daniel_days_in_min) + (semi_daniel_hours_in_min) + (semi_minutes) + (daniel_minutes))

# calculations
days_combined = (semi_daniel_minutes // (min_in_day))
hours_combined = ((semi_daniel_minutes % (min_in_day)) // (min_in_hour))
min_combined = ((semi_daniel_minutes % (min_in_day)) % (min_in_hour))

# final print
print("The total time both of them worked together is: " + str(days_combined) + " days, " + str(hours_combined) + " hours and " + str(min_combined) + " minutes")
