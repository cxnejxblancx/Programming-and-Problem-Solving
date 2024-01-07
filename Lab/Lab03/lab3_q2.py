# 12 hours --> 720 min
# 4 hours --> 240 min
# 2 hours --> 120 min
# 1 hour --> 60 min

# input
garage = input("Which garage did you park in? ")

    # pre-print
print("Please enter the hour, followed by minutes, you entered the garage (military time):")

    # input continued...
hour_entered = int(input())
minutes_entered = int(input())

    # pre-print
print("Please enter the hour, followed by minutes, you left the garage (military time):")

    # input continued...
hour_left = int(input())
minutes_left = int(input())

# variable / calculation
time_parked = (((hour_left * 60) + (minutes_left)) - ((hour_entered * 60) + (minutes_entered)))

# conditionals
if garage == "North":
    if (hour_entered <= 9) or (hour_left < 7):
        total_price = 14

    else: 
        if 240 < time_parked <= 720:
            total_price = 16

        elif 120 < time_parked <= 240:
            total_price = 10

        elif 60 < time_parked <= 120:
            total_price = 8

        elif 15 < time_parked <= 60:
            total_price = 6
            
        else:
            total_price = 0

elif garage == "South":
    if (hour_entered <= 9) or (hour_left < 7):
        total_price = 16
    else: 
        if 240 < time_parked <= 720:
            total_price = 18

        elif 120 < time_parked <= 240:
            total_price = 12

        elif 60 < time_parked <= 120:
            total_price = 10

        elif 15 < time_parked <= 60:
            total_price = 8

        else:
            total_price = 0

# print
print("Your total price for parking will be $" + str(total_price) + ".00")
