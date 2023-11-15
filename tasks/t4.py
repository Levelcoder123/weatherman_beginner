from utils.reader import get_all_data
from constants import FOLDER_PATH


def get_unique_events():
    all_unique_events = set([
        day_data[-2]
        for day_data in get_all_data(FOLDER_PATH)
        if day_data[-2]])

    return all_unique_events


print(f"Unique events are : {get_unique_events()}")
