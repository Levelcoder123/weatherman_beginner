from utils.reader import get_all_data
from utils.helpers import get_converted_date
from constants import FOLDER_PATH, IndexMapper


def get_rainy_months():
    rainy_months = []
    rain_words_list = ['rain', 'Rain', 'RAIN']

    for day_data in get_all_data(FOLDER_PATH):
        date_str = day_data[IndexMapper.DATE_STR]
        month_value = get_converted_date(date_str).month
        event = day_data[IndexMapper.EVENTS]

        if event in rain_words_list:
            rainy_months.append(month_value)

    return rainy_months


print(f"Rainy months are : {get_rainy_months()}")
