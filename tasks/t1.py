from utils.reader import weather_object
from utils.helper import get_validated_input, get_converted_date
from utils.IndexMapper import IndexMapper


class MaxTempGetter:
    all_years_data = weather_object.path_finder()

    final_maximum = 0
    may_be_maximum = 0

    @classmethod
    def maximum_temp_finder(cls, user_input):
        for index in range(len(MaxTempGetter.all_years_data)):
            date_str = MaxTempGetter.all_years_data[index][IndexMapper.DATE_STR]
            year_from_data = int(get_converted_date(date_str).year)
            MaxTempGetter.may_be_maximum = MaxTempGetter.all_years_data[index][IndexMapper.MAX_TEMP]

            if MaxTempGetter.may_be_maximum:
                MaxTempGetter.may_be_maximum = int(MaxTempGetter.may_be_maximum)

                # Check max and min temp if input match.
                if year_from_data == user_input:
                    if MaxTempGetter.may_be_maximum > MaxTempGetter.final_maximum:
                        MaxTempGetter.final_maximum = MaxTempGetter.may_be_maximum

        return MaxTempGetter.final_maximum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = MaxTempGetter.maximum_temp_finder(valid_input)
    print(f"Maximum temp of {input_string} is {return_value}")
