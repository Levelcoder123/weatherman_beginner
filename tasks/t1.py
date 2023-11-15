from utils.helpers import get_validated_input, get_data_by_year
from constants import IndexMapper


def get_max_temperature_by_year(year_from_user):
    final_maximum = int(get_data_by_year(year_from_user)[0][IndexMapper.MAX_TEMP])

    for day_data in get_data_by_year(year_from_user):
        maximum_temp = day_data[IndexMapper.MAX_TEMP]

        if maximum_temp and int(maximum_temp) > final_maximum:
            final_maximum = int(maximum_temp)

    return final_maximum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    print(f"Maximum temp of {valid_input} is {get_max_temperature_by_year(valid_input)}")
