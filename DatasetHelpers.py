import pandas as pd
from datetime import timedelta
from scheduleHelper import ScheduleHelper
from model_constants import const


class DatasetHelper:
    def __init__(self):
        self.schedule = ScheduleHelper()

    def Calculate_coefficient(self, current_time, classrooms_objets, near_time_delta):
        classrooms_coeff = 1
        for room in classrooms_objets:
            if self.schedule.is_occupied(room['id'], current_time - near_time_delta):
                distance = float(room['distance'])
                classrooms_coeff *= (1 + 1 / distance)
        return classrooms_coeff

    def get_zones_dataset_dict(self, zones_list):
        dataset_dict = {}
        for col in const.dataset_header:
            dataset_dict[col] = []
        for zone in zones_list:
            dataset_dict[const.traffic_col].append(zone[const.traffic_col])
            time_nsu = self.schedule.get_nsu_time()
            dataset_dict[const.class_col].append(self.Calculate_coefficient(time_nsu, zone['classrooms'], timedelta(minutes=30)))
            dataset_dict[const.size_col].append(zone[const.size_col])
            dataset_dict[const.sockets_col].append(zone['powerSockets'])
            dataset_dict[const.popularity_col].append(zone[const.popularity_col])
            dataset_dict[const.occupancy_col].append(zone['OccupiedSize'] / zone[const.size_col])
            dataset_dict[const.power_occupancy_col].append(zone['occupiedPowerSockets'] / zone['powerSockets'])
        return dataset_dict

    def get_features_df(self, zones_list):
        dataset_dict = self.get_zones_dataset_dict(zones_list)
        for i in range(0, len(zones_list[const.class_col])):
            zone = zones_list[i]
            time_delta = timedelta(minutes=zone['delta_time'])
            time_nsu = self.schedule.get_nsu_time() + time_delta
            dataset_dict[const.class_col][i] = self.Calculate_coefficient(time_nsu, zone['classrooms'], timedelta(minutes=30))
        return pd.DataFrame(data=dataset_dict)

    def add_new_data(self, zones_list, is_training_dataset):
        dataset_dict = self.get_zones_dataset_dict(zones_list=zones_list)
        new_dataset_df = pd.DataFrame(data=dataset_dict)

        dataset_path = const.dataset_path
        if not is_training_dataset:
            dataset_path = const.test_dataset_path
        labels_path = const.labels_path
        if not is_training_dataset:
            labels_path = const.test_labels_path

        old_dataset_df = pd.read_csv(dataset_path)
        old_dataset_df = old_dataset_df.append(new_dataset_df)
        old_dataset_df.to_csv(dataset_path, index=False)
        labels_list = []
        for zone in zones_list:
            labels_list.append(zone['OccupiedSize'])
        pd.Series(data=labels_list).to_csv(labels_path)
