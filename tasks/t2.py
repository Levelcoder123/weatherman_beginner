from utils.reader import read_weather_object, WeatherDataReader
from utils.helper import get_validated_input, get_converted_date
from utils.IndexMapper import IndexMapper


class MinTempGetter:
    all_years_data = read_weather_object.path_finder()

    final_minimum = 0
    may_be_minimum = 0

    @classmethod
    def minimum_temp_finder(cls, user_input):
        for index in range(len(MinTempGetter.all_years_data)):
            date_str = MinTempGetter.all_years_data[index][IndexMapper.DATE_STR]
            year_str = get_converted_date(date_str).year
            MinTempGetter.may_be_minimum = MinTempGetter.all_years_data[index][IndexMapper.MIN_TEMP]

            # Change min and max number into int.
            if MinTempGetter.may_be_minimum:
                MinTempGetter.may_be_minimum = int(MinTempGetter.may_be_minimum)

                # Check max and min temp if input match.
                if year_str == user_input:
                    if MinTempGetter.may_be_minimum < MinTempGetter.final_minimum:
                        MinTempGetter.final_minimum = MinTempGetter.may_be_minimum

        return MinTempGetter.final_minimum


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = MinTempGetter.minimum_temp_finder(valid_input)
    print(f"Minimum temp of {input_string} is {return_value}")
