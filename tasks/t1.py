from utils.helpers import get_validated_input, get_data_by_year
from constants import IndexMapper


def get_max_temperature_by_year(year_from_user):
    final_maximum = -1
    maximum_list = get_data_by_year(year_from_user)[IndexMapper.MAX_TEMP]

    for number in maximum_list:
        if number > final_maximum:
            final_maximum = number

    return final_maximum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    maximum_number = get_max_temperature_by_year(valid_input)
    print(f"Maximum temp of {valid_input} is {maximum_number}")
