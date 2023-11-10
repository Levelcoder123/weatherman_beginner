from utils.reader import weather_object
from datetime import datetime

all_years_data = weather_object.path_finder()
all_years = set()


def get_converted_date(date_string):
    date_format = "%Y-%m-%d"
    date_object = datetime.strptime(date_string, date_format).date()

    return date_object


def get_validated_input(user_input):
    for index in range(len(all_years_data)):
        date_str = all_years_data[index][0]
        year_str = get_converted_date(date_str).year
        all_years.add(year_str)

    # checking invalid input.
    if user_input.isdigit() and int(user_input) in all_years:
        return int(user_input)
    else:
        return False
