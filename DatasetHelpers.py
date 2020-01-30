import random
from datetime import datetime, timedelta
from scheduleHelper import ScheduleHelper
from MapTableReader import get_map_dictionary
import pandas as pd
from model_constants import const


class DatasetHelper:
    def __init__(self):
        self.schedule = ScheduleHelper()
        raw_map_dict = get_map_dictionary()
        # filter zones with no classes
        self.map_list = []
        for key in raw_map_dict:
            if self.check_zone(raw_map_dict[key]):
                self.map_list.append(raw_map_dict[key])

    def check_zone(self, zone):
        for room in zone['classrooms']:
            if self.schedule.get_classes_count(room['id']) > 0:
                return True
        return False

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
        return self.map_list[random.randint(0, len(self.map_list) - 1)]

    # None - zone don't have enough classes
    def get_random_class_time(self, rand_zone):
        for room in rand_zone['classrooms']:
            if self.schedule.get_classes_count(room['id']) > 0:
                return self.schedule.get_random_class(room['id'])
        return None

    def generate_random_dataset(self):
        dataset_dict = {}
        dataset_dict[const.traffic_col] = []
        dataset_dict[const.class_col] = []
        dataset_dict[const.size_col] = []
        dataset_dict[const.sockets_col] = []
        dataset_dict[const.popularity_col] = []
        dataset_dict[const.occupancy_col] = []

        data_entries = 1000
        # Generate random dataset
        random.seed(datetime.now().microsecond)
        near_time_delta = timedelta(minutes=25)
        for i in range(data_entries):
            is_data_good = False
            rand_zone = self.get_random_zone()
            entry_time = None
            while not is_data_good:
                entry_time = self.get_random_class_time(rand_zone)
                if entry_time == None:
                    rand_zone = self.get_random_zone()
                else:
                    is_data_good = True

            dataset_dict[const.traffic_col].append(rand_zone['traffic'])
            dataset_dict[const.size_col].append(rand_zone['size'])
            dataset_dict[const.sockets_col].append(rand_zone['powerSockets'])
            dataset_dict[const.popularity_col].append(rand_zone['popularity'])
            dataset_dict[const.class_col].append(self.Calculate_coefficient(entry_time, rand_zone['classrooms'], near_time_delta))
            dataset_dict[const.occupancy_col].append(random.randint(0, int(rand_zone['size'] * 1.5)) / rand_zone['size'])

        self.rand_dataset_df = pd.DataFrame(dataset_dict)
        self.rand_dataset_df.to_csv(r'C:\Users\user\Desktop\recreation_analitics\dataset.csv', index=False)


    def add_label_col(self, row):
        features_summ = row[const.traffic_col] * const.traffic_importance
        features_summ += row[const.size_col] * const.size_importance
        features_summ += row[const.class_col] * const.class_importance
        features_summ += row[const.popularity_col] * const.popularity_importance
        features_summ += row[const.occupancy_col] * const.occupancy_importance
        features_summ += row[const.sockets_col] * const.sockets_importance

        if features_summ < 30:
            row['label'] = const.five_min_class
        elif features_summ < 60:
            row['label'] = const.fiveteen_min_class
        elif features_summ < 80:
            row['label'] = const.thirty_min_class
        else:
            row['label'] = const.hour_min_class
        return row

    def generate_dataset_labels(self):
        self.rand_dataset_df = pd.read_csv(r'C:\Users\user\Desktop\recreation_analitics\dataset.csv')
        self.rand_dataset_df = self.rand_dataset_df.apply(self.add_label_col, axis=1)
        del self.rand_dataset_df['summ']
        self.rand_dataset_df.to_csv(r'C:\Users\user\Desktop\recreation_analitics\dataset.csv', index=False)
