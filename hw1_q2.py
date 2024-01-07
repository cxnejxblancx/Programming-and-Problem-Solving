"""
Author: Malani Snowden
Assignment / Part: HW1 - Q2
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# RATES:
    # 1 BIRTH / 7 SECONDS
    # 1 DEATH / 15 SECONDS
    # 1 IMMIGRANT / 42 SECONDS
    # 1 EMIGRANT / 1.25 MINUTES 
        # 1 MINUTE = 60 SECONDS 
        # 0.25 MINUTE = 60/4 = 15 SECONDS
            # 60 + 15 = 75
            # 1 EMIGRANT / 75 SECONDS

# Population:
    # increases with births and immigrants
    # decreases with deaths and emigrants

# input
user_year = int(input("Please enter a year greater than 2023: "))

# constants
current_population = 330109174
current_year = 2023

seconds_in_minute = 60
seconds_in_hour = (60 * (seconds_in_minute))
seconds_in_day = (24 * (seconds_in_hour))
seconds_in_year = (365 * (seconds_in_day))


# variables
years_since = (user_year - current_year)
seconds_since = (years_since * seconds_in_year)

# conversions
births = (seconds_since // 7)
deaths = (seconds_since // 15)
immigrants = (seconds_since // 42)
emigrants = (seconds_since // 75)

pop_increase = (births + immigrants)
pop_decrease = (deaths + emigrants)

new_population = (current_population + (pop_increase) - (pop_decrease))

# print
print("The population in year " + str(user_year) + " will be " + str(new_population))





