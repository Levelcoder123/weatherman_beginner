from utils.reader import get_all_data
from constants import FOLDER_PATH, IndexMapper


def get_diff_dates():
    dates_with_diff_of_7 = []

    for day_data in get_all_data(FOLDER_PATH):
        date_str = day_data[IndexMapper.DATE_STR]
        maximum_temp = day_data[IndexMapper.MAX_TEMP]
        minimum_temp = day_data[IndexMapper.MIN_TEMP]

        if (maximum_temp and minimum_temp) and int(maximum_temp) - int(minimum_temp) == 7:
            dates_with_diff_of_7.append(date_str)

    return dates_with_diff_of_7


print(f"dates with difference of 7 are : {get_diff_dates()}")
