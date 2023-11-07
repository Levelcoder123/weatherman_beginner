from python_projects.weatherman_beginner.utils.path_extractor import read_obj, ReadWeatherData

_user_input = int(input("what year's data you want to see?: (e.g => 2004)"))


class UniqueEvents(ReadWeatherData):
    year_data = read_obj.path_extract()

    unique_events = set()

    @staticmethod
    def get_unique_events():
        for index in range(len(UniqueEvents.year_data)):
            date = UniqueEvents.year_data[index][0]
            year = UniqueEvents.get_date_obj(date).year
            event = UniqueEvents.year_data[index][-2]

            if year == _user_input:
                if event != '' and event != 'Rain':
                    UniqueEvents.unique_events.add(event)
        return UniqueEvents.unique_events


print(f"Unique events in {_user_input} are : {UniqueEvents.get_unique_events()}")
