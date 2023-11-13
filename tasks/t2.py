from utils.helpers import get_validated_input, get_data_by_year
from constants import IndexMapper


def get_min_temperature_by_year(year_from_user):
    final_minimum = 0
    minimum_list = get_data_by_year(year_from_user)[IndexMapper.MIN_TEMP]

    for number in minimum_list:
        if number < final_minimum:
            final_minimum = number

    return final_minimum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    minimum_number = get_min_temperature_by_year(valid_input)
    print(f"Minimum temp of {input_string} is {minimum_number}")
