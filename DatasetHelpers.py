import random
from datetime import datetime, timedelta
from scheduleHelper import ScheduleHelper
from MapTableReader import get_map_dictionary
import pandas as pd
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

    def get_features_list(self, zones_list):
        dataset_dict = {}
        for col in const.dataset_header:
            dataset_dict[col] = []

# self.traffic_col, self.class_col,
# self.size_col, self.sockets_col, self.popularity_col,
# self.occupancy_col, self.power_occupancy_col
        for zone in zones_list:
            dataset_dict[const.traffic_col] = zone[const.traffic_col]

            time_delta = timedelta(minutes=zone['delta_time'])
            time_nsu = self.schedule.get_nsu_time() + time_delta
