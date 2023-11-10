import os


class WeatherDataReader:
    all_years_data = []

    folder_path = "../weather_files"
    all_items = os.listdir(folder_path)
    all_items_path = [os.path.join(folder_path, item) for item in all_items]

    # iterate through the paths and extract all data.
    @classmethod
    def path_finder(cls):
        for path in WeatherDataReader.all_items_path:
            with open(path, mode='r') as file:
                file_read = file.readlines()
                for line in file_read[1:]:
                    day_data = line.strip('\n').split(',')
                    WeatherDataReader.all_years_data.append(day_data)

        return WeatherDataReader.all_years_data


weather_object = WeatherDataReader.path_finder()
