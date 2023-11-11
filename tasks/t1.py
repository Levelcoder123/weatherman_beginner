from utils.reader import all_years_data
from utils.helpers import get_validated_input, get_converted_date
from constants import IndexMapper


def maximum_temp_finder(user_input):
    final_maximum = 0

    for index in range(len(all_years_data)):
        date_str = all_years_data[index][IndexMapper.DATE_STR]
        year_from_data = int(get_converted_date(date_str).year)
        may_be_maximum = all_years_data[index][IndexMapper.MAX_TEMP]

        # Change str into int.
        if may_be_maximum:
            may_be_maximum = int(may_be_maximum)

            # Check maximum temp if input match.
            if year_from_data == user_input:
                if may_be_maximum > final_maximum:
                    final_maximum = may_be_maximum

    return final_maximum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = maximum_temp_finder(valid_input)
    print(f"Maximum temp of {input_string} is {return_value}")
    
