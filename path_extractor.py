import os

# Iterate through the list of items
folder_path = "../../weatherman_project/weather_files"
all_items = os.listdir(folder_path)
files_paths = [os.path.join(folder_path, item) for item in all_items]

year_data = []


# iterate through the paths and extract all data.
def path_extractor():
    for path in files_paths:
        file_open = open(path, mode='r')
        file_read = file_open.readlines()
        for line in file_read[1:]:
            data = line.strip('\n').split(',')
            year_data.append(data)
