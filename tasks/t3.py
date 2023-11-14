from utils.reader import all_years_data
from constants import IndexMapper


def get_diff_dates():
    dates_with_diff_of_7 = []

    for day_data in all_years_data:
        date_str = day_data[IndexMapper.DATE_STR]
        maximum_temp = day_data[IndexMapper.MAX_TEMP]
        minimum_temp = day_data[IndexMapper.MIN_TEMP]

        if maximum_temp and minimum_temp:
            if int(maximum_temp) - int(minimum_temp) == 7:
                dates_with_diff_of_7.append(date_str)

    return dates_with_diff_of_7


dates_with_diff = get_diff_dates()
print(f"dates with difference of 7 are : {dates_with_diff}")
