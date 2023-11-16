from utils.reader import get_all_data
from datetime import datetime
from constants import IndexMapper, FOLDER_PATH


# To convert date string into day, month and year
def get_converted_date(date_string):
    date_format = "%Y-%m-%d"
    date_object = datetime.strptime(date_string, date_format)

    return date_object


# To take input, validate and return it
def get_validated_input(user_input):
    all_years = set()

    for index in range(len(get_all_data(FOLDER_PATH))):
        date_str = get_all_data(FOLDER_PATH)[index][IndexMapper.DATE_STR]
        year_value = get_converted_date(date_str).year
        all_years.add(year_value)

    # checking invalid input.
    if user_input.isdigit() and int(user_input) in all_years:

        return int(user_input)
    else:
        return False


# to get all data of a year and return
def get_data_by_year(year_value):
    one_year_data = []

    for day_data in get_all_data(FOLDER_PATH):
        date_str = day_data[IndexMapper.DATE_STR]
        year_from_data = get_converted_date(date_str).year

        if year_from_data == year_value:
            one_year_data.append(day_data)

    return one_year_data
