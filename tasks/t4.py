from utils.reader import all_years_data
from constants import IndexMapper


def get_unique_events():
    all_unique_events = set()

    for day_data in all_years_data:
        event = day_data[IndexMapper.EVENTS]

        if event:
            all_unique_events.add(event)

    return all_unique_events


all_events = get_unique_events()
print(f"Unique events are : {all_events}")
