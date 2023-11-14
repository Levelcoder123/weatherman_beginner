import os


def path_extractor(path_to_folder):
    all_items = os.listdir(path_to_folder)
    all_items_path = [os.path.join(path_to_folder, item) for item in all_items]

    return all_items_path


# iterate through the paths and extract all data.
def gather_all_data(path_to_folder):
    all_data = []

    for path in path_extractor(path_to_folder):
        with open(path, mode='r') as file:
            file_read = file.readlines()
            for line in file_read[1:]:
                day_data = line.strip('\n').split(',')
                all_data.append(day_data)

    return all_data


folder_path = '../weather_files'
all_years_data = gather_all_data(folder_path)
