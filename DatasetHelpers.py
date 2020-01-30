import random
from datetime import datetime, timedelta
import math
from scheduleHelper import ScheduleHelper
from MapTableReader import get_map_dictionary
import pandas as pd


class DatasetHelper:
    def __init__(self):
        self.map_dict = get_map_dictionary()
        self.schedule = ScheduleHelper()

    def Calculate_coefficient(self, current_time, classrooms_objets, near_time_delta):
        classrooms_coeff = 1
        for room in classrooms_objets:
            if self.schedule.is_occupied(room['id'], current_time - near_time_delta):
                distance = float(room['distance'])
                classrooms_coeff *= (1 + 1 / distance)
        return classrooms_coeff

    def get_random_date(self):
        time_str = str(random.randint(1, 28)) + ' ' + str(random.randint(1, 12)) + ' 2020 +0700 '
        time_str += str(random.randint(9, 22)) + ':' + str(random.randint(0, 59))
        return datetime.strptime(time_str, '%d %m %Y %z %H:%M')

    def get_random_zone(self):
        last_zone_ind = len(self.map_dict) - 1
        zone_keys = list(self.map_dict.keys())
        rand_zone_id = zone_keys[random.randint(0, last_zone_ind)]
        return self.map_dict[rand_zone_id]

    # 1 - zone don't have enough classes, 2 - time is bad
    def check_zone_occ(self, rand_zone, rand_time):
        

    def generate_random_dataset(self):
        dataset_dict = {
            'traffic': [],
            'class_coeff': [],
            'size': [],
            'sockets_size': [],
            'popularity': [],
            'currentOccupancy': []
        }
        data_entries = 1000
        # Generate random dataset
        random.seed(datetime.now().microsecond)
        near_time_delta = timedelta(minutes=25)
        for i in range(data_entries):
            entry_time = self.get_random_date()
            rand_zone = self.get_random_zone()

            dataset_dict['traffic'].append(rand_zone['traffic'])
            dataset_dict['size'].append(rand_zone['size'])
            dataset_dict['sockets_size'].append(rand_zone['powerSockets'])
            dataset_dict['popularity'].append(rand_zone['popularity'])
            dataset_dict['class_coeff'].append(self.Calculate_coefficient(entry_time, rand_zone['classrooms'], near_time_delta))
            dataset_dict['currentOccupancy'].append(random.randint(0, int(rand_zone['size'] * 1.5)) / rand_zone['size'])

        pd.DataFrame(dataset_dict).to_csv(r'C:\Users\user\Desktop\recreation_analitics\dataset.csv', index=False)
