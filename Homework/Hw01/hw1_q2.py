# RATES:
    # 1 BIRTH / 7 SECONDS
    # 1 DEATH / 15 SECONDS
    # 1 IMMIGRANT / 42 SECONDS
    # 1 EMIGRANT / 1.25 MINUTES (75 SECONDS)

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
