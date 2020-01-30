import random
from datetime import datetime, timedelta
import math
from scheduleHelper import ScheduleHelper
from MapTableReader import get_map_dictionary
import pandas as pd


def Calculate_coefficient(schedule, classrooms_objets, near_time_delta):
    classrooms_coeff = 1
    time_nsu = schedule.get_nsu_time()
    for room in classrooms_objets:
        if schedule.is_occupied(room['id'], time_nsu - near_time_delta):
            distance = float(room['distance'])
            classrooms_coeff *= (1 + 1 / distance)
            if math.isnan(classrooms_coeff):
                print(1)
    return classrooms_coeff


def generate_random_dataset():
    map_dict = get_map_dictionary()
    schedule = ScheduleHelper()

    dataset_dict = {
        'traffic': [],
        'class_coeff': [],
        'size': [],
        'sockets_size': [],
        'popularity': [],
        'currentOccupancy': []
    }
    dataset_labels = []
    data_entries = 500
    # Generate random dataset
    random.seed(datetime.now().microsecond)
    last_zone_ind = len(map_dict) - 1
    zone_keys = list(map_dict.keys())
    near_time_delta = timedelta(minutes=25)
    for i in range(data_entries):
        time_str = str(random.randint(9, 22))+':'+str(random.randint(0, 59))
        entry_time = datetime.strptime(time_str, '%H:%M')

        rand_zone_id = zone_keys[random.randint(0, last_zone_ind)]
        rand_zone = map_dict[rand_zone_id]

        dataset_dict['traffic'].append(rand_zone['traffic'])
        dataset_dict['size'].append(rand_zone['size'])
        dataset_dict['sockets_size'].append(rand_zone['powerSockets'])
        dataset_dict['popularity'].append(rand_zone['popularity'])
        dataset_dict['class_coeff'].append(Calculate_coefficient(schedule, rand_zone['classrooms'], near_time_delta))
        dataset_dict['currentOccupancy'].append(random.randint(0, int(rand_zone['size'] * 1.5)) / rand_zone['size'])

    pd.DataFrame(dataset_dict).to_csv(r'C:\Users\user\Desktop\recreation_analitics\dataset.csv', index=False)
