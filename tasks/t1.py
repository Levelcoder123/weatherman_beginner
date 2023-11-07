from python_projects.weatherman_beginner.utils.path_extractor import read_obj, ReadWeatherData

_user_input = int(input("what year's data you want to see?: (e.g => 2004)"))


class TempInYear(ReadWeatherData):
    year_data = read_obj.path_extract()

    def __init__(self):
        self.maximum = 0
        self.minimum = 0
        self.max_num = 0
        self.min_num = 0

    @staticmethod
    def get_year_max_min_num():
        for index in range(len(temp.year_data)):
            date = temp.year_data[index][0]
            year = temp.get_date_obj(date).year
            temp.max_num = temp.year_data[index][1]
            temp.min_num = temp.year_data[index][3]

            # Change min and max number into int.
            if temp.max_num and temp.min_num:
                temp.max_num = int(temp.max_num)
                temp.min_num = int(temp.min_num)

                # Check max and min temp if input match.
                if year == _user_input:
                    if temp.max_num > temp.maximum:
                        temp.maximum = temp.max_num
                    elif temp.min_num < temp.minimum:
                        temp.minimum = temp.min_num
        return temp.minimum, temp.maximum


temp = TempInYear()
minimum, maximum = temp.get_year_max_min_num()
print(f"Maximum temp of {_user_input} is {maximum} and Minimum is {minimum}")
