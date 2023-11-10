from utils.reader import weather_object
from utils.helper import get_validated_input, get_converted_date
from utils.IndexMapper import IndexMapper


class DatesWithDiff:
    year_data = weather_object.path_finder()

    dates_with_diff_of_7 = []

    @classmethod
    def get_diff_dates(cls, user_input):
        for index in range(len(DatesWithDiff.year_data)):
            date_str = DatesWithDiff.year_data[index][IndexMapper.DATE_STR]
            year_str = get_converted_date(date_str).year

            DatesWithDiff.maximum = DatesWithDiff.year_data[index][IndexMapper.MAX_TEMP]
            DatesWithDiff.minimum = DatesWithDiff.year_data[index][IndexMapper.MIN_TEMP]

            if DatesWithDiff.maximum and DatesWithDiff.minimum:  # Change str into int.
                DatesWithDiff.maximum = int(DatesWithDiff.maximum)
                DatesWithDiff.minimum = int(DatesWithDiff.minimum)

                if year_str == user_input:
                    # Check max and min temp.
                    if DatesWithDiff.maximum - DatesWithDiff.minimum == 7:
                        DatesWithDiff.dates_with_diff_of_7.append(date_str)

        return DatesWithDiff.dates_with_diff_of_7


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = DatesWithDiff.get_diff_dates(valid_input)
    print(f"dates with difference of 7 in {input_string} are : {return_value}")
