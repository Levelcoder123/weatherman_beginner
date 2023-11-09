from utils.reader import weather_object
from utils.helper import get_validated_input, get_converted_date
from utils.IndexMapper import IndexMapper


class UniqueEvents:
    all_years_data = weather_object.path_finder()

    set_of_unique_events = set()

    @classmethod
    def get_unique_events(cls, user_input):
        for index in range(len(UniqueEvents.all_years_data)):
            date_str = UniqueEvents.all_years_data[index][IndexMapper.DATE_STR]
            year_str = get_converted_date(date_str).year
            event = UniqueEvents.all_years_data[index][IndexMapper.EVENTS]

            if year_str == user_input:
                if event != '' and event != 'Rain':
                    UniqueEvents.set_of_unique_events.add(event)

        return UniqueEvents.set_of_unique_events


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = UniqueEvents.get_unique_events(valid_input)
    print(f"Unique events in {input_string} are : {return_value}")
