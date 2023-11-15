from utils.helpers import get_validated_input, get_data_by_year
from constants import IndexMapper


def get_min_temperature_by_year(year_from_user):
    final_minimum = int(get_data_by_year(year_from_user)[0][IndexMapper.MIN_TEMP])

    for day_data in get_data_by_year(year_from_user):
        minimum_temp = day_data[IndexMapper.MIN_TEMP]

        if minimum_temp and int(minimum_temp) < final_minimum:
            final_minimum = int(minimum_temp)

    return final_minimum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    print(f"Minimum temp of {input_string} is {get_min_temperature_by_year(valid_input)}")
