from utils.reader import all_years_data
from utils.helpers import get_validated_input, get_converted_date
from constants import IndexMapper


def get_diff_dates(user_input):
    dates_with_diff_of_7 = []

    for index in range(len(all_years_data)):
        date_str = all_years_data[index][IndexMapper.DATE_STR]
        year_str = int(get_converted_date(date_str).year)
        max_temp_from_data = all_years_data[index][IndexMapper.MAX_TEMP]
        min_temp_from_data = all_years_data[index][IndexMapper.MIN_TEMP]

        # Change str into int.
        if max_temp_from_data and min_temp_from_data:
            max_temp_from_data = int(max_temp_from_data)
            min_temp_from_data = int(min_temp_from_data)

            if year_str == user_input:
                # Check max and min temp.
                if max_temp_from_data - min_temp_from_data == 7:
                    dates_with_diff_of_7.append(date_str)

    return dates_with_diff_of_7


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = get_diff_dates(valid_input)
    print(f"dates with difference of 7 in {input_string} are : {return_value}")
    
