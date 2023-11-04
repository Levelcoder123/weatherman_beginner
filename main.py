from path_extractor import path_extractor, year_data
from datetime import datetime

events = set()
rainy_months = set()
dates_with_diff = []
maximum = 0
minimum = 0

user_input = int(input("what year's data you want to see?: (e.g => 2004)"))

path_extractor()

for index in range(len(year_data)):
    date_string = year_data[index][0]
    date_format = "%Y-%m-%d"

    # Use the datetime.strptime() method to parse the date string
    date_object = datetime.strptime(date_string, date_format).date()

    if date_object.year == user_input:

        year = date_object.year
        max_num = year_data[index][1]
        min_num = year_data[index][3]
        event = year_data[index][-2]
        month = date_object.month

        # Change str into int.
        if max_num and min_num:
            max_num = int(max_num)
            min_num = int(min_num)

            # Check max and min temp.
            if max_num > maximum:
                maximum = max_num
            elif min_num < minimum:
                minimum = min_num
        else:
            max_num = 0
            min_num = 0

        if event != '' and event != 'Rain':
            events.add(event)
        else:
            rainy_months.add(month)

        if maximum - minimum == 7:
            dates_with_diff.append(date_string)

print(f"Maximum temp of the year {user_input} is: {maximum}")
print(f"Minimum temp of the year {user_input} is: {minimum}")
print(f"Events in the year {user_input} are: {events}")
print(f"Rainy months in the year {user_input} are: {rainy_months}")
print(f"Dates with difference of 7 are: {dates_with_diff}")
