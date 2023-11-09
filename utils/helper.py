from utils.reader import read_weather_object, WeatherDataReader
from datetime import datetime

all_data = read_weather_object.path_finder()
all_years = set()


def get_converted_date(date):
    date_string = date
    date_format = "%Y-%m-%d"

    date_object = datetime.strptime(date_string, date_format).date()

    return date_object


def get_validated_input(user_input):
    for index in range(len(all_data)):
        date = all_data[index][0]
        year = get_converted_date(date).year
        all_years.add(year)

    # checking invalid input.
    if user_input.isdigit() and int(user_input) in all_years:
        return int(user_input)
    else:
        return False
