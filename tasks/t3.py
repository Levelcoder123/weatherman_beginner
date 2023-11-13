from utils.helpers import get_data_by_year
from constants import IndexMapper


def get_diff_dates():
    dates_with_diff_of_7 = []

    date_str = get_data_by_year()[IndexMapper.DATE_STR]
    maximum_num_list = get_data_by_year()[IndexMapper.MAX_TEMP]
    minimum_num_list = get_data_by_year()[IndexMapper.MIN_TEMP]

    # for max_num in maximum_num_list:
    #     for min_num in minimum_num_list:
    #         if max_num - min_num == 7:
    #             dates_with_diff_of_7.append(date_str)

    # return dates_with_diff_of_7
    return date_str


dates_with_diff = get_diff_dates()
print(f"dates with difference of 7 are : {dates_with_diff}")
