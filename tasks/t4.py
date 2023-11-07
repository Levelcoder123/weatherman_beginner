from python_projects.weatherman_beginner.utils.path_extractor import read_obj, ReadWeatherData

_user_input = int(input("what year's data you want to see?: (e.g => 2004)"))


class RainyMonths(ReadWeatherData):
    year_data = read_obj.path_extract()

    rainy_months = set()

    @staticmethod
    def get_rainy_months():
        for index in range(len(RainyMonths.year_data)):
            date = RainyMonths.year_data[index][0]
            year = RainyMonths.get_date_obj(date).year
            month = RainyMonths.get_date_obj(date).month
            event = RainyMonths.year_data[index][-2]

            if year == _user_input:
                if event == 'Rain':
                    RainyMonths.rainy_months.add(month)
        return RainyMonths.rainy_months


print(f"Rainy months in {_user_input} are : {RainyMonths.get_rainy_months()}")
