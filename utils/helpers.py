from utils.reader import all_years_data
from datetime import datetime
from constants import IndexMapper


# To convert date string into day, month and year
def get_converted_date(date_string):
    date_format = "%Y-%m-%d"
    date_object = datetime.strptime(date_string, date_format).date()

    return date_object


# To take input, validate and return it
def get_validated_input(user_input):
    all_years = set()

    for index in range(len(all_years_data)):
        date_str = all_years_data[index][IndexMapper.DATE_STR]
        year_str = get_converted_date(date_str).year
        all_years.add(year_str)

    # checking invalid input.
    if user_input.isdigit() and int(user_input) in all_years:
        return int(user_input)
    else:
        return False


# to get all years data and return
# def get_all_year_data():


# to get all data of a year and return
def get_data_by_year(year_from_user):
    date_list = []
    maximum_list = set()
    minimum_list = set()
    events_list = set()
    months_list = set()

    for day_data in all_years_data:
        date_str = day_data[IndexMapper.DATE_STR]
        year_from_data = get_converted_date(date_str).year
        maximum = day_data[IndexMapper.MAX_TEMP]
        minimum = day_data[IndexMapper.MIN_TEMP]
        event = day_data[IndexMapper.EVENTS]
        month_from_data = get_converted_date(date_str).month

        if year_from_data == year_from_user:
            if maximum.strip():
                maximum_list.add(int(maximum))
            if minimum.strip():
                minimum_list.add(int(minimum))
            if event.strip():
                events_list.add(event)

            months_list.add(month_from_data)
            date_list.append(date_str)

    return date_list, months_list, maximum_list, minimum_list, events_list


print(get_data_by_year(2005))
