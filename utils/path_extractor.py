import os
from datetime import datetime


class ReadWeatherData:
    _year_data = []

    def __init__(self, _folder_path):
        self._folder_path = _folder_path
        self._all_items = os.listdir(self._folder_path)
        self._files_path = [os.path.join(self._folder_path, item) for item in self._all_items]

    # iterate through the paths and extract all data.
    def path_extract(self):
        for path in self._files_path:
            with open(path, mode='r') as file:
                file_read = file.readlines()
                for line in file_read[1:]:
                    data = line.strip('\n').split(',')
                    self._year_data.append(data)
        return self._year_data

    @staticmethod
    def get_date_obj(date):
        date_string = date
        date_format = "%Y-%m-%d"

        date_object = datetime.strptime(date_string, date_format).date()

        return date_object


folder_path = "../weather_files"
read_obj = ReadWeatherData(folder_path)
