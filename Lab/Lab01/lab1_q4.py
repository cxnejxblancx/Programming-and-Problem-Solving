# input
days = int(input("How many days do you have? "))
hours = int(input("How many hours do you have? "))
minutes = int(input("How many minutes do you have? "))
seconds = int(input("How many seconds do you have? "))

# conversion factors
minutes_seconds = 60
hours_seconds = minutes_seconds * 60
days_seconds = hours_seconds * 24

# conversions
user_day_sec = (days * days_seconds)
user_hour_sec = (hours * hours_seconds)
user_min_sec = (minutes * minutes_seconds)
total_seconds = (user_day_sec + user_hour_sec + user_min_sec + seconds)

# print
print(str(days) + " Days " + str(hours) + " Hours " + str(minutes) + " Minutes and " + str(seconds) + " Seconds results in a total of " + str(total_seconds) + " Seconds.")
