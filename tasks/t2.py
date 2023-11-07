from python_projects.weatherman_beginner.utils.path_extractor import read_obj, ReadWeatherData

_user_input = int(input("what year's data you want to see?: (e.g => 2004)"))


class DifferenceOfDate(ReadWeatherData):
    year_data = read_obj.path_extract()

    dates_of_diff = []

    def __init__(self):
        self.max_num = 0
        self.min_num = 0

    @staticmethod
    def get_diff_dates():
        for index in range(len(dates.year_data)):
            date = dates.year_data[index][0]
            year = dates.get_date_obj(date).year
            dates.max_num = dates.year_data[index][1]
            dates.min_num = dates.year_data[index][3]

            if dates.max_num and dates.min_num:  # Change str into int.
                dates.max_num = int(dates.max_num)
                dates.min_num = int(dates.min_num)

                if year == _user_input:
                    # Check max and min temp.
                    if dates.max_num - dates.min_num == 7:
                        dates.dates_of_diff.append(date)
        return dates.dates_of_diff


dates = DifferenceOfDate()
dates.get_diff_dates()
print(f"dates with difference of 7 in {_user_input} are : {dates.dates_of_diff}")
