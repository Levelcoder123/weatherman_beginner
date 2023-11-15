from utils.helpers import get_validated_input, get_data_by_year
from constants import IndexMapper


def get_min_temperature_by_year(year_from_user):
    one_day_data = get_data_by_year(year_from_user)[0]
    minimum = int(one_day_data[IndexMapper.MIN_TEMP])

    for day_data in get_data_by_year(year_from_user):
        may_be_minimum = day_data[IndexMapper.MIN_TEMP]

        if may_be_minimum and int(may_be_minimum) < minimum:
            minimum = int(may_be_minimum)

    return minimum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    print(f"Minimum temp of {input_string} is {get_min_temperature_by_year(valid_input)}")
