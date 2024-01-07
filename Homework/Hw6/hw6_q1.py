# PART 1: CONVERTING TO DECIMAL TIME
def get_decimal_time(hour, minute, second):
    # variables
    conventional_secs_min = 60
    conventional_mins_hour = 60
    french_secs_min = 100
    french_mins_hour = 100

    # conversions
    total_conventional_seconds = (hour * (conventional_secs_min * conventional_mins_hour)) + (minute * conventional_secs_min) + second
    
    french_hours = total_conventional_seconds // (french_secs_min * french_mins_hour)
    french_minutes = (total_conventional_seconds % (french_secs_min * french_mins_hour)) // french_secs_min
    french_seconds = (total_conventional_seconds % (french_secs_min * french_mins_hour)) % french_secs_min

    # variable
    french_time = f"{french_hours}:{french_minutes}:{french_seconds}"

    # return
    return french_time


# PART 2: CONVERTING TO REVOLUTIONARY DATES
def get_decimal_date(month, day, year):
    # condtional --> account for dates outside of french range
    if day == 31:
        if month != 12:
            month += 1
        else:
            month -= 11

    # conditionals --> month
    if month == 1:
        french_month = "Nivôse"
    elif month == 2:
        french_month = "Pluviôse"
    elif month == 3:
        french_month = "Ventôse"
    elif month == 4:
        french_month = "Germinal"
    elif month == 5:
        french_month = "Floréal"
    elif month == 6:
        french_month = "Prairial"
    elif month == 7:
        french_month = "Messidor"
    elif month == 8:
        french_month = "Thermidor"
    elif month == 9:
        french_month = "Fructidor"
    elif month == 10:
        french_month = "Vendémiaire"
    elif month == 11:
        french_month = "Brumaire"
    elif month == 12:
        french_month = "Frimaire"

    # conditionals --> decade
    if 20 < day <= 30:
        décade = 3
    elif 10 < day <= 20:
        décade = 2
    else: # check for (day <= 10) AND (day == 31)
        décade = 1

    # variables
    french_year = year - 1792
    french_date = f"{day} {french_month} Year {french_year}, Décade {décade}"

    # return
    return french_date


# PART 3: PUTTING IT ALL TOGETHER
def get_french_datetime(gregorian_datetime):
    space_index = gregorian_datetime.find(" ")
    gregorian_time = gregorian_datetime[:space_index]
    gregorian_date = gregorian_datetime[(space_index + 1): ]

    # variables
        # time 
            # locate colons
    colon_index1 = gregorian_time.find(":")
    colon_index2 = gregorian_time.find(":", (colon_index1 + 1))
            # separate hour, minute, second
    gregorian_hour = int(gregorian_time[:colon_index1])
    gregorian_minute = int(gregorian_time[(colon_index1 + 1):colon_index2])
    gregorian_second = int(gregorian_time[(colon_index2 + 1):])
        # date
            # locate forwardslashes
    slash_index1 = gregorian_date.find("/")
    slash_index2 = gregorian_date.find("/", (slash_index1 + 1))
            # separate month, day, year
    gregorian_month = int(gregorian_date[:slash_index1])
    gregorian_day = int(gregorian_date[(slash_index1 + 1):slash_index2])
    gregorian_year = int(gregorian_date[(slash_index2 + 1):])

    # call functions
    french_time = get_decimal_time(gregorian_hour, gregorian_minute, gregorian_second)
    french_date = get_decimal_date(gregorian_month, gregorian_day, gregorian_year)

    # variable
    french_datetime = f"{french_time}\n{french_date}"

    # return
    return french_datetime


# test the functions
def main():
    gregorian_datetime = "2:50:20 2/12/2022"
    french_datetime = get_french_datetime(gregorian_datetime)
    print(french_datetime)

main()
