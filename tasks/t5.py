from utils.reader import read_weather_object, WeatherDataReader
from utils.helper import get_validated_input, get_converted_date
from utils.IndexMapper import IndexMapper


class RainyMonths:
    all_years_data = read_weather_object.path_finder()

    set_of_rainy_months = set()

    @classmethod
    def get_rainy_months(cls, user_input):
        for index in range(len(RainyMonths.all_years_data)):
            date = RainyMonths.all_years_data[index][IndexMapper.DATE_STR]
            year = get_converted_date(date).year
            month = get_converted_date(date).month
            event = RainyMonths.all_years_data[index][IndexMapper.EVENTS]

            if year == user_input:
                if event == 'Rain':
                    RainyMonths.set_of_rainy_months.add(month)

        return RainyMonths.set_of_rainy_months


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = RainyMonths.get_rainy_months(valid_input)
    print(f"Rainy months in {input_string} are : {return_value}")
