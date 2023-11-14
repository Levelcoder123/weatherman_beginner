from utils.reader import all_years_data
from utils.helpers import get_validated_input, get_converted_date
from constants import IndexMapper


def get_rainy_months():
    all_rainy_months = []
    rain_list = ['rain', 'Rain', 'RAIN']

    for day_data in all_years_data:
        date_str = day_data[IndexMapper.DATE_STR]
        month_str = get_converted_date(date_str).month
        event = day_data[IndexMapper.EVENTS]

        if event in rain_list:
            all_rainy_months.append(month_str)

    return all_rainy_months


months_of_rain = get_rainy_months()
print(f"Rainy months are : {months_of_rain}")
