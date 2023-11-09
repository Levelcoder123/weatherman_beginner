import os


class WeatherDataReader:
    all_years_data = []

    def __init__(self, _folder_path):
        self._folder_path = _folder_path
        self._all_items = os.listdir(self._folder_path)
        self._files_path = [os.path.join(self._folder_path, item) for item in self._all_items]

    # iterate through the paths and extract all data.
    def path_finder(self):
        for path in self._files_path:
            with open(path, mode='r') as file:
                file_read = file.readlines()
                for line in file_read[1:]:
                    data = line.strip('\n').split(',')
                    self.all_years_data.append(data)

        return self.all_years_data


folder_path = "../weather_files"
weather_object = WeatherDataReader(folder_path)
