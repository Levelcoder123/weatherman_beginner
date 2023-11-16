from utils.reader import get_all_data
from constants import FOLDER_PATH, IndexMapper


def get_unique_events():
    return set([
        day_data[IndexMapper.EVENTS]
        for day_data in get_all_data(FOLDER_PATH)
        if day_data[IndexMapper.EVENTS]])


print(f"Unique events are : {get_unique_events()}")
