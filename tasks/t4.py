from utils.reader import all_years_data
from utils.helpers import get_validated_input, get_converted_date
from constants import IndexMapper


def get_unique_events(user_input):
    all_unique_events = set()

    for index in range(len(all_years_data)):
        date_str = all_years_data[index][IndexMapper.DATE_STR]
        year_str = get_converted_date(date_str).year
        event = all_years_data[index][IndexMapper.EVENTS]

        if year_str == user_input:
            if event != '' and event != 'Rain':
                all_unique_events.add(event)

    return all_unique_events


input_string = input("what year's data you want to see?: (e.g => 2004)")
valid_input = get_validated_input(input_string)

if valid_input is False:
    print("This isn't a valid input !!!. Please type a valid input(e.g => 2004 to 2016)")
else:
    return_value = get_unique_events(valid_input)
    print(f"Unique events in {input_string} are : {return_value}")
    
