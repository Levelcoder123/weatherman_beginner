from utils.helpers import get_validated_input, get_data_by_year
from constants import IndexMapper


def get_max_temperature_by_year(year_from_user):
    one_day_data = get_data_by_year(year_from_user)[0]
    maximum = int(one_day_data[IndexMapper.MAX_TEMP])

    for day_data in get_data_by_year(year_from_user):
        may_be_maximum = day_data[IndexMapper.MAX_TEMP]

        if may_be_maximum and int(may_be_maximum) > maximum:
            maximum = int(may_be_maximum)

    return maximum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    print(f"Maximum temp of {valid_input} is {get_max_temperature_by_year(valid_input)}")
